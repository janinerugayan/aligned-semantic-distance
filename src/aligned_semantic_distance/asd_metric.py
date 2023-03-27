from collections import namedtuple
import numpy as np
from dtw import dtw
from scipy.spatial import distance
import torch
from tabulate import tabulate
from aligned_semantic_distance.exceptions import DuplicateLayersException, IncorrectLayersException

try:
    from IPython.display import HTML, display
except ImportError:
    HTML, display = None, None


def get_asd_output(reference_text: str, hypothesis_text: str, model, tokenizer, layers: list[int] = []):
    """
    Calculates the aligned semantic distance of reference and hypothesis text pair.
    
    :param reference_text: Reference text for the ASR transcription. 
    :param hypothesis_text: Hypothesis text from the ASR model. 
    :param model: BERT model used to calculate the ASD score. 
    :param tokenizer: Tokenizer of the BERT model. 
    :param layers: List of hidden layer numbers considered in the extraction of the reference and hypothesis 
    embedding vectors. Function uses all the layers of the BERT model by default (Default: []). 

    :return: The calculated ASD score which is the accumulated distance of the optimal alignment normalized 
    by the total number of tokens in the reference embedding vector. It also returns the aligned tokens and token 
    embeddings for both the reference and hypothesis.
    :rtype: namedtuple 
    
    """
    
    # input checks
    if layers:
        if len(set(layers)) != len(layers):
            raise DuplicateLayersException("Duplicate layer numbers declared in the list.")
        for num in layers:
            if num > model.config.num_hidden_layers or num < 1:
                raise IncorrectLayersException("Input layer number unacceptable for the model.")
    
    # tokenize the ref & hyp texts
    tokenized_ref = tokenizer(reference_text, padding=True, truncation=True, max_length=512, return_tensors="pt")
    tokenized_hyp = tokenizer(hypothesis_text, padding=True, truncation=True, max_length=512, return_tensors="pt")
    
    # extract token ids
    ref_input_ids = tokenized_ref["input_ids"].squeeze()
    hyp_input_ids = tokenized_hyp["input_ids"].squeeze()
    
    # get ref & hyp embedding vectors 
    with torch.no_grad():
        model_output_ref = model(**tokenized_ref, output_hidden_states=True)
        model_output_hyp = model(**tokenized_hyp, output_hidden_states=True)                          
    layers_reference = []
    layers_hypothesis = []
    if layers:
        for num in layers:
            layers_reference.append(model_output_ref.hidden_states[num].squeeze())
            layers_hypothesis.append(model_output_hyp.hidden_states[num].squeeze())
    else:
        for i in range(1, model.config.num_hidden_layers + 1):
            layers_reference.append(model_output_ref.hidden_states[i].squeeze())
            layers_hypothesis.append(model_output_hyp.hidden_states[i].squeeze())
    ref_embedding_sequence = torch.stack(layers_reference).mean(dim=0)
    hyp_embedding_sequence = torch.stack(layers_hypothesis).mean(dim=0)
    
    # calculate ASD score by using DTW alignment and normalizing by ref embedding seq length
    alignment = dtw(x=hyp_embedding_sequence, y=ref_embedding_sequence, dist_method=distance.cosine, 
                    keep_internals=True)
    asd_score = (alignment.distance / (len(ref_embedding_sequence)))
    
    # for printing token alignment
    hyp_alignment_idxs = alignment.index1
    ref_alignment_idxs = alignment.index2
    
    ref_alignment_input_ids = np.empty(len(ref_alignment_idxs), dtype=int)
    hyp_alignment_input_ids = np.empty(len(hyp_alignment_idxs), dtype=int)
    for i, index in enumerate(ref_alignment_idxs):
        ref_alignment_input_ids[i] = (ref_input_ids[index])
    for i, index in enumerate(hyp_alignment_idxs):
        hyp_alignment_input_ids[i] = (hyp_input_ids[index])
    ref_alignment_tokens = tokenizer.convert_ids_to_tokens(torch.from_numpy(ref_alignment_input_ids))
    hyp_alignment_tokens = tokenizer.convert_ids_to_tokens(torch.from_numpy(hyp_alignment_input_ids))
    
    ref_alignment_token_embeddings = [ref_embedding_sequence[index] for index in ref_alignment_idxs]
    hyp_alignment_token_embeddings = [hyp_embedding_sequence[index] for index in hyp_alignment_idxs]
    
    # output 
    Asd = namedtuple("ASD", ["score", "ref_tokens", "hyp_tokens", 
                             "ref_token_embeddings", "hyp_token_embeddings"])
    asd_output = Asd(score=asd_score, 
                     ref_tokens=ref_alignment_tokens, 
                     hyp_tokens=hyp_alignment_tokens,
                     ref_token_embeddings=ref_alignment_token_embeddings, 
                     hyp_token_embeddings=hyp_alignment_token_embeddings)
    
    return asd_output


def in_notebook():
    try:
        from IPython import get_ipython
        if 'IPKernelApp' not in get_ipython().config:  # pragma: no cover
            return False
    except ImportError:
        return False
    except AttributeError:
        return False
    return True


def print_alignment(asd_output):
    """
    Prints the resulting token-wise alignment of the reference and hypothesis. 
    
    :param asd_output: Return value of the get_asd_output function. It contains the ASD score/value, list of aligned reference 
    and hypothesis tokens, list of aligned reference and hypothesis token embeddings. 
    :type asd_output: namedtuple
    """
    
    # copying list of aligned tokens for printing
    ref_token_list = asd_output.ref_tokens.copy()
    ref_token_list.insert(0, "REF:")
    hyp_token_list = asd_output.hyp_tokens.copy()
    hyp_token_list.insert(0, "HYP:")
    alignment_table = [ref_token_list, hyp_token_list]
    
    if in_notebook():
        table = tabulate(alignment_table, tablefmt="html")
        display(HTML(table))
    else:
        table = tabulate(alignment_table, tablefmt="jira")
        print(table)
