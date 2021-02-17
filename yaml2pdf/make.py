#!/usr/bin/python3

import codecs
import os

import yaml
from pybars import Compiler
from weasyprint import HTML


def make_document_from_yaml(template, yaml_file):
    make(template, yaml.safe_load(codecs.open(yaml_file, encoding="utf-8")))


def make_document_from_directory(template, directory):
    for yaml_file in os.listdir(directory):
        make_document_from_yaml(
            template,
            os.path.join(directory, yaml_file),
        )


def make(template, document):
    with codecs.open(template, encoding="utf-8") as index_file:
        html_text = Compiler().compile(index_file.read())(document)
        HTML(string=html_text, base_url=template).write_pdf(
            document["filename"]
        )
