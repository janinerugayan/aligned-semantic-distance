# Aligned Semantic Distance
This package implements the semantic distance for automatic speech recognition (ASR) first introduced in

*Janine Rugayan and Torbjørn Svendsen and Giampiero Salvi* (2022). **Semantically Meaningful Metrics for Norwegian ASR Systems**. In Interspeech, pp. 2283-2287<br>
[![DOI:10.21437/Interspeech.2022-817](https://zenodo.org/badge/DOI/10.21437/Interspeech.2022-817.svg)](https://doi.org/10.21437/Interspeech.2022-817)

A more detailed analysis of the metric was later included in

*Janine Rugayan and Giampiero Salvi and Torbjørn Svendsen* (2023). **Perceptual and Task-Oriented Assessment of a Semantic Metric for ASR Evaluation**. In Interspeech, pp. 2158--2162<br>
[![DOI:10.21437/Interspeech.2023-1778](https://zenodo.org/badge/DOI/10.21437/Interspeech.2023-1778.svg)](https://doi.org/10.21437/Interspeech.2023-1778)

If you use this code in your research, please acknowledge us by citing at least one of the above papers.

## Local installation
Download the code or clone the repository and move to the repository's root directory.
If your python installation requires the use of virtual environments, then run
```
python3 -m venv asdvenv
source asdvenv/bin/activate
```
Then install by running

```
python3 -m pip install .
```
Alternatively, you can install direclty from git (but this requires a working authentication):
```
python3 -m pip install "git+https://github.com/janinerugayan/aligned-semantic-distance.git"
```
Check installation with
```
python3 -m pip show aligned_semantic_distance
```

## Usage

First load a large language model to be used for the word embeddings.
For example, using [NorBERT2](https://huggingface.co/ltg/norbert2):
```
from transformers import BertModel, AutoTokenizer
metric_modelname = 'ltg/norbert2'
model = BertModel.from_pretrained(metric_modelname)
tokenizer = AutoTokenizer.from_pretrained(metric_modelname)
```

Import the package.
```
import aligned_semantic_distance as asd
```
Define a reference transcription and an ASR hypothesys transcription, for example:
```
reference_text = 'mange tror at ordet øl på norsk kjem ifra det engelske ale'
hypothesis_text = 'mange trur at ordet øl på norsk kjem ifra det engelske aill'
```
Choose which layers from the large language model are used for the word embeddings (this is a list of one or more layer indexes):
```
layers = [5, 6, 7, 8]
```

Run the semantic metric:
```
# function returns a named tuple 
asd_output = asd.get_asd_output(reference_text, hypothesis_text, model, tokenizer, layers)
```
The function returns a namedtouple with the following fields:
* `score`: the global semantic distance between reference and hypothesis
* `ref_tokens`: list of tokens used to represent the reference text after alignment
* `hyp_tokens`: list of tokens used to represent the hypothesis text after alignment
* `ref_token_embeddings`: array of embeddings for reference text after alignment
* `hyp_token_embeddings`: array of embeddings for hypothesis text after alignment

If you want pretty print the token alignment run:
```
asd.print_alignment(asd_output)
```
