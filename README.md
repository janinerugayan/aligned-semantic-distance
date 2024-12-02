# Aligned Semantic Distance
This package implements the semantic distance for automatic speech recognition (ASR) first introduced in

*Janine Rugayan and Torbjørn Svendsen and Giampiero Salvi* (2022). **Semantically Meaningful Metrics for Norwegian ASR Systems**. In Interspeech, pp. 2283-2287<br>
[![DOI:10.21437/Interspeech.2022-817](https://zenodo.org/badge/DOI/10.21437/Interspeech.2022-817.svg)](https://doi.org/10.21437/Interspeech.2022-817)

A more detailed analysis of the metric was later included in

*Janine Rugayan and Giampiero Salvi and Torbjørn Svendsen* (2023). **Perceptual and Task-Oriented Assessment of a Semantic Metric for ASR Evaluation**. In Interspeech, pp. 2158--2162<br>
[![DOI:10.21437/Interspeech.2023-1778](https://zenodo.org/badge/DOI/10.21437/Interspeech.2023-1778.svg)](https://doi.org/10.21437/Interspeech.2023-1778)

If you use this code in your research, please acknowledge us by citing at least one of the above papers.

## Local installation
Download the code or clone the repository. Then in the repository's root directory, run

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

Define the following parameters to start using the metric:
```
model = 
tokenizer = 
```

Import the package. It requires the reference and hypothesis text. You can define which output layers (by layer number) of the BERT model are to be considered. 
```
import aligned_semantic_distance as asd

# function returns a named tuple 
asd_output = asd.get_asd_output(reference_text, hypothesis_text, model, tokenizer, layers)

print(asd_output["score"])

# prints the resulting token-wise alignment of the reference and hypothesis
asd.print_alignment(asd_output)
```
