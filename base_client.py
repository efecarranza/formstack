import requests
import json

class BaseClient(object):
    def __init__(self):
        self.key = 'bfd1c87bef70098cfaabae583892f342'
        self.serverUrl = 'https://www.formstack.com/api/v2/'
        self.form_id = '2143752'
        self.first_name_id = '36379032'
        self.last_name_id = '36491672'
        self.views_id = '36491671'
        self.headers = { 'Authorization': 'Bearer %s' % self.key,
                    'Accept': 'application/json',
                    'Content-type': 'application/json' }

    def send_get_request_form(self):
        url = self.serverUrl + 'form/%s/submission.json' % self.form_id
        response = requests.get(url, headers=self.headers, data=data)
        submissions = response.json()['submissions']
        return submissions

    def send_get_request_submission(self, submission_id):
        url = self.serverUrl + 'submission/%s.json' % submission_id
        response = requests.get(url, headers=self.headers)
        submission = response.json()
        return submission


    def send_post_request(self): # , form_id, data --> add these fields to take
        data = { 'field_%s' % self.first_name_id: 'Fermin',
               'field_%s' % self.last_name_id: 'Carranza',
               'field_%s' % self.views_id: 'Socialist'
        }
        url = self.serverUrl + 'form/%s/submission.json' % self.form_id
        response = requests.post(url, headers=self.headers, data=data)
        return response

if __name__ == "__main__":
    client = BaseClient()
    client.send_get_request_form()
    # client.send_post_request()
