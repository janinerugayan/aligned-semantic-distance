from aligned_semantic_distance import get_asd_output, print_alignment
from transformers import BertModel, AutoTokenizer
import pytest
from aligned_semantic_distance.exceptions import DuplicateLayersException, IncorrectLayersException


modelname = 'ltg/norbert2'
model = BertModel.from_pretrained(modelname)
tokenizer = AutoTokenizer.from_pretrained(modelname)

ref_text = "Jeg er sulten"
hyp_text = "Jeg er trøtt"

duplicate_layers = [1, 1, 2, 3]
incorrect_layers = [1, 5, 13]
correct_layers = [5, 6, 7, 8]

@pytest.mark.xfail(raises=DuplicateLayersException)
def test_duplicates():
    get_asd_output(ref_text, hyp_text, model, tokenizer, duplicate_layers)

@pytest.mark.xfail(raises=IncorrectLayersException)
def test_incorrect_layers():
    get_asd_output(ref_text, hyp_text, model, tokenizer, incorrect_layers)

def test_correct_layers():
    get_asd_output(ref_text, hyp_text, model, tokenizer, correct_layers)

def test_empty_layer_list():
    get_asd_output(ref_text, hyp_text, model, tokenizer, [])

