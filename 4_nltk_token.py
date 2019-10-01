__author__ = "Otacilio Maia"
__version__ = "1.0.0"

import nltk

sentence = "O S.E.C é um evento arretado. Valeu pessoal!"
splited = sentence.split()
tokens = nltk.word_tokenize(sentence)

print("\n\nA versão com split")
print(splited)

print("\n\nA versão com tokens")
print(tokens)
print("\n")