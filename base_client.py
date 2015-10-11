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

    def generate_submissions_list(self, submissions_json):
        submissions_list = []
        for submission in submissions_json:
            id = submission.get('id')
            submissions_list.append(id)
        return submissions_list

    def get_submissions_list(self):
        url = self.serverUrl + 'form/%s/submission.json' % self.form_id
        response = requests.get(url, headers=self.headers)
        submissions = response.json()['submissions']
        submissions_list = self.generate_submissions_list(submissions)
        return submissions_list

    def get_voter_details(self, submission):
        voter_data = {}
        for data in submission:
            if self.first_name_id in data.values():
                voter_data['first_name'] = data['value']
            elif self.last_name_id in data.values():
                voter_data['last_name'] = data['value']
            elif self.views_id in data.values():
                voter_data['views'] = data['value']
        return voter_data

    def get_submission_details(self, submission_id): # , submission_id
        url = self.serverUrl + 'submission/%s.json' % submission_id
        response = requests.get(url, headers=self.headers)
        submission = response.json()
        voter_data = self.get_voter_details(submission['data'])
        voter_data['submission_id'] = submission_id
        return voter_data

    def update_submission(self, submission_id, views):
        data = { 'field_%s' % self.views_id: views }
        url = self.serverUrl + 'submission/%s.json' % submission_id
        response = requests.put(url, headers=self.headers, data=data)
        return response.status_code

    def send_submission(self, first_name, last_name, views): # , form_id, data --> add these fields to take
        data = { 'field_%s' % self.first_name_id: first_name,
                 'field_%s' % self.last_name_id: last_name,
                 'field_%s' % self.views_id: views
        }
        url = self.serverUrl + 'form/%s/submission.json' % self.form_id
        response = requests.post(url, headers=self.headers, data=data)
        return response.status_code

if __name__ == "__main__":
    client = BaseClient()
    # client.get_submissions_list()
    client.get_submission_details()
