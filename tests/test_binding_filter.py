import unittest
import os
import tempfile
from filecmp import cmp
import sys
import py_compile

from pvactools.lib.binding_filter import BindingFilter
from .test_utils import *

#python -m unittest tests/test_binding_filter.py
class BindingFilterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        #locate the bin and test_data directories
        cls.binding_filter_path = os.path.join(pvactools_directory(), "pvactools", "lib", "binding_filter.py")
        cls.test_data_path= os.path.join(pvactools_directory(), "tests", "test_data", "binding_filter")

    def module_compiles(self):
        self.assertTrue(py_compile.compile(self.binding_filter_path))

    def test_binding_filter_runs_and_produces_expected_output(self):
        output_file = tempfile.NamedTemporaryFile()
        self.assertFalse(BindingFilter(
            os.path.join(
                self.test_data_path,
                'Test.combined.parsed.tsv'
            ),
            output_file.name,
            500,
            0,
            'median',
            False,
            False,
            None,
        ).execute())
        self.assertTrue(cmp(
            output_file.name,
            os.path.join(self.test_data_path, "Test.filtered.binding.tsv"),
            False
        ))

    def test_binding_filter_with_percentile_runs_and_produces_expected_output(self):
        output_file = tempfile.NamedTemporaryFile()
        self.assertFalse(BindingFilter(
            os.path.join(
                self.test_data_path,
                'Test.combined.parsed.tsv'
            ),
            output_file.name,
            500,
            0,
            'median',
            False,
            False,
            0.1,
        ).execute())
        self.assertTrue(cmp(
            output_file.name,
            os.path.join(self.test_data_path, "Test.filtered.binding.percentile.tsv"),
            False
        ))
