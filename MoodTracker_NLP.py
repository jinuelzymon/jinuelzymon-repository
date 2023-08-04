import nltk
import contract_word as cont
from nltk.corpus.reader import WordListCorpusReader
from nltk.tokenize import sent_tokenize
from nltk.tokenize import RegexpTokenizer
from removalrepeat import Rep_word_removal
repeat_char = Rep_word_removal()
r = WordListCorpusReader('.',['C:/Users/ACER/OneDrive/Documents/MoodTrackerJournal/Notes.txt'])
orig_txt = sent_tokenize(r.raw())

f = open('texthere.txt','w')
for sent in orig_txt:
     contract = cont.contracted(sent)
     contract_token = contract.split()
     for word in contract_token:
         clean_word1 = repeat_char.replace(word)
         if clean_word1 == '.':
            f.write(f".\n")
         else:
            f.write(f"{clean_word1} ")
f.close()

f1 = open("texthere.txt", "r")
text = f1.read()
print(text)
f1.close()
