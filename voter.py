class Voter(object):
    DEMOCRAT_STATS = { "Socialist": 0.90,
                       "Liberal": 0.75,
                       "Neutral": 0.50,
                       "Conservative": 0.25,
                       "Tea party": 0.10 }

    REPUBLICAN_STATS = { "Tea party": 0.90,
                         "Conservative": 0.75,
                         "Neutral": 0.50,
                         "Liberal": 0.25,
                         "Socialist": 0.10 }

    def __init__(self, first_name, last_name, views, submission_id = ''):
        self.first_name = first_name
        self.last_name = last_name
        self.views = views
        self.vote = None
        self.submission_id = submission_id

    def decide_vote(self, politician, random_num):
        party = politician.party
        if party == 'Democrat':
            likelihood = self.DEMOCRAT_STATS[self.views]
        elif party == 'Republican':
            likelihood = self.REPUBLICAN_STATS[self.views]

        if (random_num <= likelihood):
            self.vote = politician.party
        elif self.vote == None:
            self.vote = 'null'
