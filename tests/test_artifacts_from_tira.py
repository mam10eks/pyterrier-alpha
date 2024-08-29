import pytest
import unittest
import pandas as pd
from pyterrier_alpha.artifact import from_url

try:
    # this is not yet in the main branch of tira until everything is stable
    # this test requires this branch to be installed:
    # pip3 install 'https://github.com/tira-io/tira/archive/pyterrier-artifacts.zip#&subdirectory=python-client'
    import tira
    TIRA_CLIENT_INSTALLED = True
except:
    TIRA_CLIENT_INSTALLED = False

class TestArtifactsFromTira(unittest.TestCase):
    @pytest.mark.skipif(not TIRA_CLIENT_INSTALLED, reason="This test requires the tira-python client.")
    def test_foo(self):
        expected = {
            'qid': '1',
            'docno': 'clueweb12-0200wb-79-18105',
            'name': 'sparse_cross_encoder',
            'rank': 1,
            'score': 8.310153007507324 
        }
        sparse_cross_encoder_transformer = from_url('tira://clueweb12/touche-2020-task-2/fschlatt/sparse-cross-encoder-4-512')
        actual = sparse_cross_encoder_transformer(pd.DataFrame([{'qid': '1'}]))
	
        self.assertEqual(expected, actual.iloc[0].to_dict())

    # TODO: Add more tests, also for different types

