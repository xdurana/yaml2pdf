# yaml2pdf

Simple PDF generator from HTML templates and YAML data files

![Python application](https://github.com/xdurana/yaml2pdf/workflows/Python%20application/badge.svg)

## Synopsis

Generate a single PDF from a YAML file

```bash
$ python -m make from-yaml --template [FILE] --yaml-file [FILE]
```

Generate one PDF from every YAML file on the given directory

```bash
$ python -m make from-directory --template [FILE] --directory [DIRECTORY]
```

## Example

```bash
$ python yaml2pdf.py from-yaml --template samples/template/index.html
  --yaml-file samples/data/invoices.yaml
```

```bash
$ python yaml2pdf.py make from-directory --template samples/template/index.html
  --directory samples/data
```

## Create virtual environment

```bash
python3 -m venv .venv
.venv/bin/python setup.py install
```

## Run tests

```bash
.venv/bin/python3 -m tests.test_make
```