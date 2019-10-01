# Before execute run
# pip install -U spacy
# python -m spacy download pt

__author__ = "Otacilio Maia"
__version__ = "1.0.0"

import spacy

nlp = spacy.load('pt')
my_doc = nlp('O S.E.C. é um evento incrível!')

for token in my_doc:
    print(token, token.pos_)

# ADJ: adjective
# ADP: adposition
# ADV: adverb
# AUX: auxiliary
# CCONJ: coordinating conjunction
# DET: determiner
# INTJ: interjection
# NOUN: noun
# NUM: numeral
# PART: particle
# PRON: pronoun
# PROPN: proper noun
# PUNCT: punctuation
# SCONJ: subordinating conjunction
# SYM: symbol
# VERB: verb
# X: other