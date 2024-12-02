# Aligned Semantic Distance
This package implements the semantic distance for automatic speech recognition (ASR) first introduced in

*Janine Rugayan and Torbjørn Svendsen and Giampiero Salvi* (2022) **Semantically Meaningful Metrics for Norwegian ASR Systems}**. In Interspeech, 2283-2287
[![DOI:10.21437/Interspeech.2022-817](https://zenodo.org/badge/DOI/10.21437/Interspeech.2022-817.svg)](https://doi.org/10.21437/Interspeech.2022-817)

A more detailed analysis of the metric was later included in
```
@inproceedings{rugayan23_interspeech,
  title     = {Perceptual and Task-Oriented Assessment of a Semantic Metric for ASR Evaluation},
  author    = {Janine Rugayan and Giampiero Salvi and Torbjørn Svendsen},
  year      = {2023},
  booktitle = {INTERSPEECH 2023},
  pages     = {2158--2162},
  doi       = {10.21437/Interspeech.2023-1778},
  issn      = {2958-1796}
}
```
If you use this code in your research, please achnowledge us by citing at least one of the above papers.

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

## Testing the package

```
tox

tox -e py38
tox -e py310
```

## Running linter

```
tox -e lint
```

## Building docs

```
tox -e docs
```

## Build package

Make sure you have build package installed:
```
python3 -m pip install --upgrade build
```

Now build your package:
```
python3 -m build
```

```
ls -la dist
```

## Upload package to PYPI

Register on https://pypi.org/

Make sure you have twine package installed:
```
python3 -m pip install --upgrade twine
```

Upload package data
```
python3 -m twine upload --repository testpypi dist/*
```

Cleanup
```
rm -rv dist/*.{whl,tar.gz}
```

