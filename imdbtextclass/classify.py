import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import pandas as pd
text="""Hello Mr. Smith, how are you doing today? The weather is great, and city is awesome.
The sky is pinkish-blue. You shouldn't eat cardboard"""
tokenized_word=word_tokenize(text)
# print(tokenized_word)
freqdist = FreqDist(tokenized_word)
stop_w = set(stopwords.words("english"))
filtered_sent = []
for w in tokenized_word:
    if w not in stop_w:
        filtered_sent.append(w)
# print(filtered_sent)


ps = PorterStemmer
lem = nltk.WordNetLemmatizer()
stemmed_words = []
# for w in filtered_sent:
#     stemmed_words.append(ps.stem(w))
# lemmatized_words = []
# for w in filtered_sent:
#     lemmatized_words.append(lem.lemmatize(w,"v"))

nltk.pos_tag(tokenized_word)

data = pd.read_csv("train.tsv", sep='\t')

