#!/usr/bin/python3

import click

from yaml2pdf.make import make_document_from_directory, make_document_from_yaml


@click.group()
def ciit():
    pass


@ciit.command()
@click.option("--template", type=str)
@click.option("--yaml-file", type=click.Path(exists=True))
def from_yaml(template, yaml_file):
    make_document_from_yaml(template, yaml_file)


@ciit.command()
@click.option("--template", type=str)
@click.option("--directory", type=click.Path(exists=True))
def from_directory(template, directory):
    make_document_from_directory(template, directory)


def main():
    ciit(obj={})


if __name__ == "__main__":
    main()
