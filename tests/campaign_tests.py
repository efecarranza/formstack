import unittest
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from campaign import Campaign

campaign = Campaign()
mock_submissions_json = {'total': '2',
                         'submissions': [
                            {'remote_addr': '50.115.104.50',
                              'read': '1',
                              'timestamp': '2015-10-09 17:17:31',
                              'longitude': '-80.193702697754',
                              'user_agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
                              'payment_status': '',
                              'latitude': '25.774299621582',
                              'id': '218459301'},
                            ],
                         'pages': 1
                        }
mock_submission_ids = ['218459301']
mock_submission = [{'field': '36379032', 'value': 'Fermin'}, {'field': '36491672', 'value': 'Carranza'}, {'field': '36491671', 'value': 'Liberal'}]
mock_voter_data = {'first_name': 'Fermin', 'last_name': 'Carranza', 'views': 'Liberal'}

class CampaignTests(unittest.TestCase):
    def test_generate_politician_instances_should_return_two_politicians(self):
        self.failUnless(len(campaign.politicians) == 2)

    def test_generate_voter_instances_should_return_0_or_greater(self):
        self.failIf(len(campaign.voters) < 0)

def main():
    unittest.main()

if __name__ == '__main__':
    main()
