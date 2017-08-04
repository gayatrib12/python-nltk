import nltk.tokenize as nk
#from nltk.tokenize import sent_tokenize, word_tokenize

text = "Hello, this is a trial here! Hello Mr. Smith, how are you doing today? The weather is great, and Python is awesome. The sky is pinkish-blue. You shouldn't eat cardboard."
print ('sent_tokenize' +nk.sent_tokenize(text))
print ('word_tokenize' +nk.word_tokenize(text))