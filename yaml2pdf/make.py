#!/usr/bin/python3

import codecs
import os

import yaml
from pybars import Compiler
from weasyprint import HTML


def make_document_from_yaml(template, yaml_file, output_dir):
    make(template, yaml.safe_load(codecs.open(yaml_file, encoding="utf-8")))


def make_document_from_directory(template, directory, output_dir):
    for yaml_file in os.listdir(directory):
        make_document_from_yaml(
            template, os.path.join(directory, yaml_file), output_dir=output_dir
        )


def make(template, document, output_dir):
    with codecs.open(template, encoding="utf-8") as index_file:
        html_text = Compiler().compile(index_file.read())(document)
        HTML(string=html_text, base_url=template).write_pdf(
            os.path.join(output_dir, document["filename"])
        )
