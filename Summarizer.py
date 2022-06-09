import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from collections import Counter
import en_core_web_lg
from heapq import nlargest
import youtube_transcript_api
from youtube_transcript_api import YouTubeTranscriptApi

link = "https://www.youtube.com/watch?v=bz7yYu_w2HY" 
unique_id = link.split("=")[-1]
sub = YouTubeTranscriptApi.get_transcript(unique_id)  
subtitle = " ".join([x['text'] for x in sub])

subtitle = " ".join(subtitle.split())
print(subtitle)

#nlp = spacy.load('en_core_web_lg')
nlp = en_core_web_lg.load()

print("\n\n\nSUMMARY\n\n\n")
doc = nlp(subtitle)
a = len(list(doc.sents))

keyword = []
stopwords = list(STOP_WORDS)
pos_tag = ['PROPN','ADJ','NOUN','VERB']
for token in doc:
  if(token.text in stopwords or token.text in punctuation):
    continue
  if(token.pos_ in pos_tag):
    #Lemmatization in spaCy is just extracting the processed doc from the spaCy NLP pipeline. 
    keyword.append(token.lemma_)
    #print(token.text,token.lemma_)

freq_word = Counter(set(keyword))
freq_word.most_common(4)

max_freq = Counter(keyword).most_common(1)[0][1]
for word in freq_word.keys():
  freq_word[word] = (freq_word[word]/max_freq)
freq_word.most_common(4)

sent_strength = {}
for sent in doc.sents:
  for word in sent:
    if word.text in freq_word.keys():
      if sent in sent_strength.keys():
        sent_strength[sent] += freq_word[word.text]
      else:
        sent_strength[sent] = freq_word[word.text]

summarized_sentences = nlargest(int(a/5),sent_strength,key = sent_strength.get)

final_sentences = [w.text for w in summarized_sentences]
summary = ' '.join(final_sentences)
print(summary) 
