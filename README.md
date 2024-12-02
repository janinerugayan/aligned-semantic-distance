# Aligned Semantic Distance

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

