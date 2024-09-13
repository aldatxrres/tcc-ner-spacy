import spacy
from spacy import displacy

spacy.require_gpu() 
# require_gpu will raise an error if no GPU is available.

# mudar paleta de cores de cada entidade
colors = {
    "SINTOMA|SINAL": "linear-gradient(90deg, #AA9CFC, #FC9CE7)",
    "DOENÇA|SINDROME": "linear-gradient(90deg, #AA9CFC, #FC9CE7)",
    "PARTE DO CORPO|ORGAO": "linear-gradient(90deg, #AA9CFC, #FC9CE7)",
    "PROCEDIMENTO": "linear-gradient(90deg, #AA9CFC, #FC9CE7)",
    "DISPOSITIVO MEDICO": "linear-gradient(90deg, #AA9CFC, #FC9CE7)",
    "CELULA|DISFUNCAO MOLECULAR": "linear-gradient(90deg, #AA9CFC, #FC9CE7)",
    "PROCEDIMENTO DIAGNOSTICO": "linear-gradient(90deg, #AA9CFC, #FC9CE7)",
    "FUNCAO FISIOLOGICA": "linear-gradient(90deg, #AA9CFC, #FC9CE7)",
    "CONCLUSAO": "linear-gradient(90deg, #AA9CFC, #FC9CE7)",
    "ANTIBIOTICO": "linear-gradient(90deg, #AA9CFC, #FC9CE7)",
    "LOCALIZACAO NO CORPO OU REGIAO": "linear-gradient(90deg, #AA9CFC, #FC9CE7)",
    "RESULTADO LABORATORIO OU TESTE": "linear-gradient(90deg, #AA9CFC, #FC9CE7)",
    "MEMBRO FAMILIAR": "linear-gradient(90deg, #AA9CFC, #FC9CE7)",
    "ACAO DE CUIDADO": "linear-gradient(90deg, #AA9CFC, #FC9CE7)",
    "FARMACO|HORMONIO|PROTEINA": "linear-gradient(90deg, #AA9CFC, #FC9CE7)",
    "LESAO": "linear-gradient(90deg, #AA9CFC, #FC9CE7)",
    "ENVENENAMENTO": "linear-gradient(90deg, #AA9CFC, #FC9CE7)",
    "BACTERIA": "linear-gradient(90deg, #AA9CFC, #FC9CE7)",
}

nlp = spacy.load("C:\\Users\\aldat\\OneDrive\\Documents\\[TCC] NER\\trained-pipeline-tcc")

with open("c:\\Users\\aldat\\OneDrive\\Documents\\[TCC] NER\\Projeto spaCy\\cbis-ner-spacy\\clinical-reports\\cc_039.txt", encoding="utf-8") as file:
    texto = file.read()

doc = nlp(texto)
displacy.serve(doc, style='ent', page=True, options={"colors": colors})
