import unittest
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from base_client import BaseClient
import requests
import httpretty

client = BaseClient()
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

class BaseClientTests(unittest.TestCase):
    @httpretty.activate
    def test_generates_list_of_submission_ids(self):
        id_list = client.generate_submissions_list(mock_submissions_json['submissions'])
        self.failUnless(id_list == mock_submission_ids)

    def test_generate_voter_details(self):
        voter_data = client.get_voter_details(mock_submission)
        self.failUnless(voter_data == mock_voter_data)

    def test_put_request_to_update_voter(self):
        httpretty.register_uri(httpretty.PUT, "http://www.formstack.com/api/v2/submission/%s.json" % mock_submission_ids[0],
            status=200)
        response = requests.put("http://www.formstack.com/api/v2/")
        assert response.status_code == 200

    def test_post_request_to_submit_survey(self):
        httpretty.register_uri(httpretty.POST, "http://www.formstack.com/api/v2/form/%s/submission.json" % mock_submission_ids[0],
            status=200)
        response = requests.post("http://www.formstack.com/api/v2/")
        assert response.status_code == 200

    def test_get_submissions_list(self):
        httpretty.register_uri(httpretty.GET, "http://www.formstack.com/api/v2/form/%s/submission.json" % '12345',
            body='12345')
        response = requests.get("http://www.formstack.com/api/v2/")
        assert response.status_code == 200

    def test_get_submission_details(self):
      httpretty.register_uri(httpretty.GET, "http://www.formstack.com/api/v2/submission/%s.json" % mock_submission_ids[0],
        body='[{"title": "Test Deal"}]',
        content_type="application/json",
        accept="application/json")
      response = requests.get('http://www.formstack.com/api/v2/')
      assert response.status_code == 200

def main():
    unittest.main()

if __name__ == '__main__':
    main()
