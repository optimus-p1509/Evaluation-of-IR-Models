import json
import urllib.request
import os
#os.chdir('output')
#outfn = 'path_to_your_file.txt'
#count = 1
models = ["BM25","VSM","DFR"]
for model in models:
    outf = open(model + '_updated_boost.txt', 'w')
    count = 1
    with open('testqueries.txt', encoding="utf-8") as f:
        for line in f:
            query=line[4:len(line)]
            query = line.strip('\n').replace(':', '')
            query = urllib.parse.quote(query)
            weight_en=1.6
            weight_de=1.6
            weight_ru=1.6
            original_lang =(query[5:7])
            if original_lang=="en":
                weight_en=2.0    
            elif original_lang=="de":
                weight_de=2.0
            elif original_lang=="ru":
                weight_ru=2.0

            print(original_lang)
            query = line.strip('\n').replace(':', '')
            query = urllib.parse.quote(query)
            weights = 'tweet_hashtags^2.5%20text_en^'+str(weight_en)+'%20text_de^'+str(weight_de)+'%20text_ru^'+str(weight_ru)+'%20tweet_urls^0'
            #print(query)
            #inurl = 'http://localhost:8983/solr/'+model+'Core/select?&q=' + query + '&fl=id%2Cscore&wt=json&indent=true&rows=20'
            #inurl = 'http://localhost:8983/solr/'+model+'Core/select?q=' + query + '&fl=id%2Cscore&wt=json&indent=true&rows=20'
            inurl = 'http://localhost:8983/solr/'+ model +'Core/select?defType=dismax&fl=id,%20score&indent=on&q='+str(query)+'&qf='+weights+'&rows=20&wt=json'
            print(inurl)
            qid = str(count).zfill(3)
            
            outf = open(model + '.txt', 'a+')
            data = urllib.request.urlopen(inurl).read()
            docs = json.loads(data.decode('utf-8'))['response']['docs']
            rank = 1
            outf1 = open(model + qid[2] +'.txt', 'a+')
            for doc in docs:
                outf1.write(str(qid) + ' ' + 'Q0' + ' ' + str(doc['id']) + ' ' + str(rank) + ' ' + str(doc['score']) + ' ' + model + '\n')
                outf.write(str(qid) + ' ' + 'Q0' + ' ' + str(doc['id']) + ' ' + str(rank) + ' ' + str(doc['score']) + ' ' + model + '\n')
                rank += 1
            outf.close()
            count += 1
