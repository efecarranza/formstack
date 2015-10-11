import unittest
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from politician import Politician

class PoliticianTests(unittest.TestCase):
    def test_generates_list_of_submission_ids(self):
        politician = Politician('First', 'Last', 'Democrat')
        display_politician = 'First Last - Democrat'
        self.failUnless(display_politician == politician.list_politician())

def main():
    unittest.main()

if __name__ == '__main__':
    main()
