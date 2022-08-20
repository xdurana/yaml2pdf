# yaml2pdf

Simple `PDF` generator from `HTML` templates and `YAML` data files

![Python application](https://github.com/xdurana/yaml2pdf/workflows/Python%20application/badge.svg)

## Synopsis

Generate a single `PDF` from a `YAML` file

```bash
python3 -m yaml2pdf from-yaml \
  --template [FILE] \
  --yaml-file [FILE] \
  --output-dir [OUTPUT]
```

Generate one `PDF` from every `YAML` file in the given directory

```bash
python3 -m yaml2pdf from-directory \
  --template [FILE] \
  --directory [DIRECTORY] \
  --output-dir [OUTPUT]
```

## Example

```bash
python3 yaml2pdf -m from-yaml \
  --template yaml2pdf/samples/template/index.html \
  --yaml-file yaml2pdf/samples/data/F21-00009.yaml \
  --output-dir output
```

```bash
python3 -m yaml2pdf from-directory \
  --template yaml2pdf/samples/template/index.html \
  --directory yaml2pdf/samples/data \
  --output-dir output
```

## Installation

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 setup.py install
```
