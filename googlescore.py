# -*- coding: iso-8859-1 -*-
from bs4 import BeautifulSoup
import requests
import re
from collections import defaultdict

def query_google_se(keywords):
    kwords = "+".join(keywords)
    prefix = 'http://www.google.se/search?q='
    query = prefix + kwords
    return query

list_of_kwords = []
list_of_kwords.append([40,'surdeg','matbröd','salt'])
list_of_kwords.append([30,'surdeg','råg','jäst'])
list_of_kwords.append([20,'matbröd','nybakat'])
list_of_kwords.append([10,'vetemjöl','baksirap'])

google_rank_value = [15,13,11,9,7,6,5,4,3,2,1]
googlescore_count = defaultdict(int)

for kword in list_of_kwords:
#for i in range(len(list_of_kwords)):
    searchstr = query_google_se(kword[1:])
    print searchstr + "     Search Value : " + str(kword[0])
    r = requests.get(searchstr)
    soup = BeautifulSoup(r.content)
    google_rank_count = 0
    for div in soup('div',attrs={'id':'search'}):
        for h in div('h3',attrs={'class':'r'}):
            for a in h.find_all('a'):
                m = re.search('://(.+?)/', str(a))
                if m:
                    found = m.group(1)
                    google_rank_count += 1
                    print found + "    rank: "+str(google_rank_count)
                    googlescore_count[found] += (kword[0] * google_rank_value[google_rank_count])
                    
print 80*"*"
print "**********************        GOOGLE SCORE        ******************************"
print 80*"*"
for r in sorted(googlescore_count, key = googlescore_count.get, reverse=True):
    print "Domän %r får %s poäng" % (r, googlescore_count[r])

    

    


