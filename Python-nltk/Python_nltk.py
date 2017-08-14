import nltk.tokenize as nk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

#basic splitting into tokens
text = "Hello, this is a trial here! Hello Mr. Smith, how are you doing today? The weather is great, and Python is awesome. The sky is pinkish-blue, You shouldn't eat cardboard."
#print (nk.sent_tokenize(text))
#print (nk.word_tokenize(text))

#for j in nk.sent_tokenize(text):
#    print (j)

#for i in nk.word_tokenize(text):
#    print (i)


#working on stop words
example_text =  "This is a sample sentence, showing off the stop words filtration."
stop_words = set(stopwords.words('english'))
word_tokens = nk.word_tokenize(example_text)

#filtered_sentence = [w for w in word_tokens if not w in stop_words]
filtered_sentence = []

for w in word_tokens:
    if w not in word_tokens:
        filtered_sentence.append(w)

print (word_tokens)
print (filtered_sentence)