import spacy
from spacy.training import Example, offsets_to_biluo_tags
import os

def clean_annotations(text, entities):
    cleaned_entities = []
    for start, end, label in entities:
        entity_text = text[start:end].strip()  # Remove espaços em branco
        start = text.find(entity_text)  # recalcula o índice de início
        if start != -1:  # verifica se entidade foi encontrada corretamente
            end = start + len(entity_text)  # recalcula o índice de fim
            cleaned_entities.append((start, end, label))
        else:
            print(f"Erro: entidade '{entity_text}' não encontrada no texto.")
    return cleaned_entities

def load_train_data_from_directory(directory_path):
    train_data = []

    for filename in os.listdir(directory_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory_path, filename)
            
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
                try:
                    example = eval(content)
                    text = example[0]
                    annotations = example[1]
                    entities = annotations['entities']

                    # Limpar as entidades e verificar o alinhamento
                    cleaned_entities = clean_annotations(text, entities)
                    doc = nlp.make_doc(text)
                    tags = offsets_to_biluo_tags(doc, cleaned_entities)
                    
                    if '-' in tags:  
                        print(f"Desalinhamento no arquivo: {filename}")
                    else:
                        # adiciona as anotações corrigidas ao dado de treino
                        train_data.append((text, {'entities': cleaned_entities}))
                except SyntaxError as e:
                    print(f"Erro ao processar o arquivo {filename}: {e}")
    return train_data

directory_path = "annoted-clinical-reports"

nlp = spacy.blank("pt")  
ner = nlp.add_pipe("ner")

train_data = load_train_data_from_directory(directory_path)

# adiciona todos as tags das entidades ao NER
for text, annotations in train_data:
    for ent in annotations.get("entities"):
        if not nlp.get_pipe("ner").has_label(ent[2]):
            ner.add_label(ent[2])

optimizer = nlp.begin_training()

# treina novo modelo
for itn in range(100):
    losses = {}
    for text, annotations in train_data:
        doc = nlp.make_doc(text)
        example = Example.from_dict(doc, annotations)
        try:
            nlp.update([example], sgd=optimizer, losses=losses)
        except Exception as e:
            print(f"Erro no update para o texto: {text}\nErro: {e}")
    print(f"Iteração {itn + 1}, Perdas: {losses}")

# Salva novo modelo treinado
nlp.to_disk("C:\\Users\\aldat\\OneDrive\\Documents\\[TCC]NER\\trained-pipeline-tcc")

# treinar diferentes modelos com proporções diferentes para teste/treino 
# usar primeira poucos documentos pra treino e teste, analisar o comportamento e depois identificar quais arquivos estão com problema de processamento
# possivelmente irei tratar esses arquivos ou eliminá-los 