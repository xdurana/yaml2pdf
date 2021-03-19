# yaml2pdf

Simple PDF generator from HTML templates and YAML data files

![Python application](https://github.com/xdurana/yaml2pdf/workflows/Python%20application/badge.svg)

## Synopsis

Generate a single PDF from a YAML file

```bash
$ .venv/bin/python yaml2pdf.py  from-yaml --template [FILE] --yaml-file [FILE]
```

Generate one PDF from every YAML file on the given directory

```bash
$ .venv/bin/python yaml2pdf.py  from-directory --template [FILE] --directory [DIRECTORY]
```

## Example

```bash
$ .venv/bin/python yaml2pdf.py from-yaml --template yaml2pdf/samples/template/index.html --yaml-file yaml2pdf/samples/data/F21-00009.yaml
```

```bash
$ .venv/bin/python yaml2pdf.py from-directory --template yaml2pdf/samples/template/index.html --directory yaml2pdf/samples/data
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