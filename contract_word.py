import re
def contracted(phrase):
     # specific
     phrase = re.sub("will not","won\'t", phrase)
     phrase = re.sub("can not","can\'t", phrase)
     # general
     phrase = re.sub("(\w+) are", "\g<1>\'re", phrase)
     phrase = re.sub( "(\w+) is","\g<1>\'s", phrase)
     phrase = re.sub( "(\w+) has","\g<1>\'s", phrase)
     phrase = re.sub("(\w+) will","\g<1>\'ll" ,phrase)
     phrase = re.sub("(\w+) not","\g<1>n\'t", phrase)
     phrase = re.sub("(\w+) have","\g<1>\'ve", phrase)
     phrase = re.sub( "(\w+) am","\g<1>\'m", phrase)
     return phrase
