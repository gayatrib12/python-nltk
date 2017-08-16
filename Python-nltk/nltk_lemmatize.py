import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import sent_tokenize, PunktSentenceTokenizer
from nltk.corpus import gutenberg

lemmatizer = WordNetLemmatizer()

#find nltk location and use particular corpus file
print(nltk.__file__)
sample = gutenberg.raw("bible-kjv.txt")
tok = sent_tokenize(sample)

for x in range(5):
    print(tok[x])

print(lemmatizer.lemmatize("cats"))
print(lemmatizer.lemmatize("cacti"))
print(lemmatizer.lemmatize("rocks"))

print(lemmatizer.lemmatize("better"))
print(lemmatizer.lemmatize("better", pos="a"))
print(lemmatizer.lemmatize("best", pos="a"))
print(lemmatizer.lemmatize("run"))
print(lemmatizer.lemmatize("run", pos="v"))