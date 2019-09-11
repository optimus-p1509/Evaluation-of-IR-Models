# -*- coding: utf-8 -*-


import json
# if you are using python 3, you should 
import urllib.request 
#import urllib2


# change the url according to your own corename and query
inurl = 'http://localhost:8983/solr/test/select?q=*%3A*&fl=id%2Cscore&wt=json&indent=true&rows=20'
outfn = 'test_scores.txt'


# change query id and IRModel name accordingly
qid = '001'
IRModel='default'
outf = open(outfn, 'w+')
#data = urllib2.urlopen(inurl)
# if you're using python 3, you should use
data = urllib.request.urlopen(inurl)

docs = json.load(data)['response']['docs']
# the ranking should start from 1 and increase
rank = 1
for doc in docs:
    outf.write(qid + ' ' + 'Q0' + ' ' + str(doc['id']) + ' ' + str(rank) + ' ' + str(doc['score']) + ' ' + IRModel + '\n')
    rank += 1
outf.close()
