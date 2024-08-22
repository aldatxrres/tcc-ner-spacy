import spacy
from spacy.training import Example

train_data = [
    
]

nlp = spacy.blank("pt")
ner = nlp.add_pipe("ner")

for text, annotations in train_data:
    for ent in annotations.get("entities"):
        ner.add_label(ent[2])

optimizer = nlp.begin_training()

for itn in range(100):
    for text, annotations in train_data:
        doc = nlp.make_doc(text)
        example = Example.from_dict(doc, annotations)
        nlp.update([example], sgd=optimizer)

nlp.to_disk("C:\\Users\\aldat\\OneDrive\\Documents\\[TCC]NER\\trained-pipeline-tcc")