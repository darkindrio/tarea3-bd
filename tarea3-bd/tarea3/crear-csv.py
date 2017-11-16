from mrjob.job import MRJob
from mrjob.step import MRStep
from mrjob.protocol import JSONValueProtocol
import re
import itertools
aux = [] 
class UsersCount(MRJob):
    INPUT_PROTOCOL = JSONValueProtocol
    def mapper_userid(self, _, line):
	aux.append([line['business_id'], line['stars']])
	if 'categories' in line:
	    for rev in aux:
		if rev[0] == line['business_id']:
		    for cat in line['categories']:
			yield [cat, rev[1]]

	    #yield [line['business_id'], line['stars']]
 
    def reducer(self, key, values):
	aux_gen = list(values)
        yield [key, aux_gen]
 
    def max_reducer(self, stat, values):
        TEMP = [values]
        yield [stat,max(values)]
 
    def steps(self):
        return [MRStep(mapper=self.mapper_userid, reducer = self.reducer)]
 
 
if __name__ == '__main__':
    UsersCount.run()
