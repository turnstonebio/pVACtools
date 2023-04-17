import unittest
from Bio.Blast import NCBIWWW

from tests.utils import *


class BlastApiStatusTest(unittest.TestCase):
    def test_netchop_api_runs_and_returns_expected_value(self):
        result_handle = NCBIWWW.qblast("blastp", "refseq_select_prot", "AAIMYVPALGWEFLAFTRLTSELNFLLQEID", entrez_query="Homo Sapiens [Organism]", word_size=7, gapcosts='32767 32767')
        expected_file_name = os.path.join(pvactools_directory(), 'api_status_tests', 'blast_response.xml')
        with open(expected_file_name, 'r') as expected_fh:
            actual_content = response.read()
            expected_content = expected_fh.read()
            self.assertEqual(expected_content, actual_content)