import sys
import operator
from collections import Counter
from textblob import TextBlob, Word

with open (sys.argv[1], "r") as myfile:
    data=myfile.read()
    data=data.decode('utf-8', 'replace')

    #freq=Counter(data.split()).most_common()
    #topten=freq[:10]
    #bottomten=freq[-10:]

    blob=TextBlob(data)
    nps=blob.np_counts

    print sorted(nps.iteritems(), key=operator.itemgetter(1))
    print "sample size: " + str(len(blob))
    print blob.sentiment
