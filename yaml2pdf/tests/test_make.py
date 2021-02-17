import os
import unittest

from make import make_document_from_directory, make_document_from_yaml


class TestYAML2PDF(unittest.TestCase):
    def test_single(self):
        make_document_from_yaml(
            os.path.join(
                os.path.dirname(__file__), "../samples/template/index.html"
            ),
            os.path.join(
                os.path.dirname(__file__), "../samples/data/invoices.yaml"
            ),
        )

    def test_directory(self):
        make_document_from_directory(
            os.path.join(
                os.path.dirname(__file__), "../samples/template/index.html"
            ),
            os.path.join(os.path.dirname(__file__), "../samples/data"),
        )


if __name__ == "__main__":
    unittest.main()
