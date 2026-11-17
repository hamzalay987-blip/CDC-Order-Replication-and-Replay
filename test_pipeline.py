import os
import sys
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from main import run

class ProjectTests(unittest.TestCase):
    def setUp(self):
        os.chdir(ROOT)

    def test_representative_sample(self):
        result=run()
        expected={'events_seen': 5, 'live_orders': {'A': 25}, 'last_sequences': {'A': 3, 'B': 2}}
        for key,value in expected.items():
            self.assertEqual(result[key],value, f'Mismatch on {key}')

    def test_replay_consistency(self):
        self.assertEqual(run(),run())

if __name__=='__main__':
    unittest.main()
