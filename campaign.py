from __future__ import division
from base_client import BaseClient
from voter import Voter
from politician import Politician
from bcolors import bcolors
import random

class Campaign(object):
    VALID_VIEWS = ['Socialist', 'Neutral', 'Conservative', 'Tea Party', 'Liberal']
    def __init__(self):
        print bcolors.WARNING + 'Loading 2016 Election Campaign Manager...' + bcolors.ENDC
        self.client = BaseClient()
        self.submissions_list = self.client.get_submissions_list()
        self.voters = self.generate_voter_instances(self.submissions_list)
        self.politicians = self.generate_politician_instances()
        self.votes_democrat = []
        self.votes_republican = []

    def list_submitted_surveys(self):
        for index, voter in enumerate(self.voters):
            print '%s - %s %s - %s - Voter ID: %s' % (index, voter.first_name, voter.last_name, voter.views, voter.submission_id)

    def generate_voter_instances(self, submissions):
        all_voters = []
        for submission in submissions:
            voter_data = self.client.get_submission_details(submission)
            voter = Voter(voter_data['first_name'], voter_data['last_name'], voter_data['views'], voter_data['submission_id'])
            all_voters.append(voter)
        return all_voters

    def generate_politician_instances(self):
        politicians = []
        democrat = Politician('Hilary', 'Clinton', 'Democrat')
        politicians.append(democrat)
        republican = Politician('Donald', 'Trump', 'Republican')
        politicians.append(republican)
        return politicians

    def submit_vote(self, first_name, last_name, views):
        response = self.client.send_submission(first_name, last_name, views)
        return response

    def create_voter(self):
        print 'Alright, let\'s create a voter'
        first_name = raw_input('What is the voter\'s first name?').lower().capitalize()
        last_name = raw_input('Ok, what is the voter\'s last name?').lower().capitalize()
        print 'For this survey, please select one of the following views:'
        for view in self.VALID_VIEWS:
            print view
        views = raw_input().lower().capitalize()
        voter = Voter(first_name, last_name, views)
        response = self.submit_vote(first_name, last_name, views)
        if response == 200:
            self.voters.append(voter)
        else:
            print 'There was an error submitting your survey, please try again later.'
        return

    def update_voter_views(self):
        print 'Please indicate the ID (it\'s the value of the first column) of the voter whose views you\'d like to update:'
        self.list_submitted_surveys()
        voter_id = raw_input('\n-->')
        submission_id = self.voters[int(voter_id)].submission_id
        print 'Alright, now select the new views for this voter.'
        for view in self.VALID_VIEWS:
            print view
        views = raw_input('\n-->').lower().capitalize()
        response = self.client.update_submission(submission_id, views)
        if response == 200:
            self.voters[int(voter_id)].views = views
            print 'Voter views updated successfully.'
        else:
            print 'There was an error while submitting your request, please try again later.'

    def vote(self):
        for politician in self.politicians:
            for voter in self.voters:
                rnd = random.random()
                voter.decide_vote(politician, rnd)

        self.tally()

    def tally(self):
        votes_democrat = 0
        votes_republican = 0
        votes_null = 0
        for voter in self.voters:
            if voter.vote == 'Democrat':
                votes_democrat += 1
            elif voter.vote == 'Republican':
                votes_republican += 1
            else:
                votes_null += 1

        print '\n'
        print 'Based on our estimations derived from this survey, the 2016 Election would go to:'
        if votes_democrat > votes_republican:
            print bcolors.OKBLUE
            print self.politicians[0].list_politician()
            print bcolors.ENDC
        elif votes_republican > votes_democrat:
            print bcolors.FAIL
            print self.politicians[1].list_politician()
            print bcolors.ENDC
        else:
            print 'It is impossible for us to derive a potential winner based on the amount of surveys collected at this time.'

        total_votes = votes_democrat + votes_republican + votes_null
        pct_democrat = votes_democrat / total_votes * 100
        pct_republican = votes_republican / total_votes * 100
        pct_null = votes_null / total_votes * 100

        print 'The statistics breakdown is as follows:'
        print bcolors.OKBLUE + '%0.2f percent voted democrat' % pct_democrat
        print bcolors.FAIL + '%0.2f percent voted republican' % pct_republican
        print bcolors.WARNING + '%0.2f percent abstained from voting' % pct_null
        print bcolors.ENDC

    def start_simulation(self):
        print '\nWelcome to the' + bcolors.FAIL + ' 2016' + bcolors.OKBLUE + ' Election ' + bcolors.FAIL + ' Campaign Manager \n'
        print bcolors.ENDC + 'The campagin manager lets you submit surveys on behalf of voters, ' + \
               'update information submitted by users, and run simulations to see the most likely candidate to' + \
               'become the President of the United States in 2016.'
        print 'Please select onf the following options:'
        while True:
            print bcolors.WARNING + '[LIST VOTERS] [LIST CANDIDATES] [SUBMIT VOTE] [UPDATE SUBMISSION] [RUN SIMULATION] [EXIT]' + bcolors.ENDC
            response = raw_input().upper()
            if response == 'SUBMIT VOTE':
                self.create_voter()
            elif response == 'LIST VOTERS':
                self.list_submitted_surveys()
            elif response == 'LIST CANDIDATES':
                for politician in self.politicians:
                    politician.list_politician()
            elif response == 'UPDATE SUBMISSION':
                self.update_voter_views()
            elif response == 'RUN SIMULATION':
                self.vote()
            elif response == 'EXIT':
                print 'Thank you for using the 2016 Campagin Manager'
                exit()
            else:
                print 'Please select a valid command'

if __name__ == "__main__":
    campaign = Campaign()
    campaign.start_simulation()



