class Politician(object):
    def __init__(self, first_name, last_name, party):
        self.first_name = first_name
        self.last_name = last_name
        self.party = party

    def list_politician(self):
        print '%s %s - %s' % (self.first_name, self.last_name, self.party)
        return '%s %s - %s' % (self.first_name, self.last_name, self.party)

