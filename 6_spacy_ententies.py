import spacy

nlp = spacy.load('pt')
doc = nlp('Gildo lanches é o melhor lugar de Recife para lanchar, fica perto da Poli')

for ent in doc.ents:
    print(ent.text, ent.label_)