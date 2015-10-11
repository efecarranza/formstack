import unittest
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from voter import Voter
from politician import Politician

mocked_democrat = Politician('Democrat', 'One', 'Democrat')
mocked_republican = Politician('Republican', 'One', 'Republican')
mocked_democrat_for_null = Politician('Democrat', 'Two', 'Democrat')


class VoterTests(unittest.TestCase):
    def test_decide_vote_should_return_null(self):
        voter = Voter('first_name', 'last_name', 'Liberal', '12345')
        voter.decide_vote(mocked_democrat_for_null, 0.99)
        self.failUnless(voter.vote == 'null')

    def test_decide_vote_should_return_democrat(self):
        voter = Voter('first_name', 'last_name', 'Liberal', '12345')
        voter.decide_vote(mocked_democrat, 0.70)
        self.failUnless(voter.vote == 'Democrat')

    def test_decide_vote_should_return_republican(self):
        voter = Voter('first_name', 'last_name', 'Liberal', '12345')
        voter.decide_vote(mocked_republican, 0.20)
        self.failUnless(voter.vote == 'Republican')



def main():
    unittest.main()

if __name__ == '__main__':
    main()
