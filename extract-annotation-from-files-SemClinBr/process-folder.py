import os
from bs4 import BeautifulSoup

# pasta onde estão os arquivos XML
input_dir = "files-SemClinBr"
output_dir = "annoted-clinical-reports"

# cria pasta de saída se não existir
os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(input_dir):
    if filename.endswith(".xml"):
        input_file_path = os.path.join(input_dir, filename)
        
        with open(input_file_path, "r", encoding="utf-8") as file:
            xml = file.read()

        soup = BeautifulSoup(xml, 'xml')

        # extrai o conteúdo do relato de caso
        clinical_report_content = soup.find("TEXT").text

        # lista para armazenar as entidades
        entities = []

        # lista para armazenar as categorias das entidades que são válidas pro meu contexto 
        categories_spacy =  [
            "SINTOMA|SINAL",
            "DOENÇA|SINDROME",
            "PARTE DO CORPO|ORGAO",
            "PROCEDIMENTO",
            "DISPOSITIVO MEDICO",
            "CELULA|DISFUNCAO MOLECULAR",
            "PROCEDIMENTO DIAGNOSTICO",
            "FUNCAO FISIOLOGICA",
            "CONCLUSAO",
            "ANTIBIOTICO",
            "LOCALIZACAO NO CORPO OU REGIAO",
            "RESULTADO LABORATORIO OU TESTE",
            "MEMBRO FAMILIAR",
            "ACAO DE CUIDADO",
            "FARMACO|HORMONIO|PROTEINA",
            "LESAO",
            "ENVENENAMENTO",
            "BACTERIA"
        ]

        categories_sem_clin = [
            "Sign or Symptom",
            "Disease or Syndrome",
            "Body Part, Organ, or Organ Component",
            "Therapeutic or Preventive Procedure",
            "Medical Device",
            "Cell or Molecular Dysfunction",
            "Diagnostic Procedure",
            "Physiologic Function",
            "Finding",
            "Antibiotic",
            "Body Location or Region",
            "Laboratory or Test Result",
            "Family Group",
            "Health Care Activity",
            "Pharmacologic Substance|Hormone|Amino Acid, Peptide, or Protein",
            "Injury or Poisoning",
            "Bacterium"
        ]

        for tags in soup.find_all("TAGS"):
            for annotation in tags.find_all("annotation"):
                category = annotation.get("tag")

                if category == categories_sem_clin[0]: 
                    start_position = int(annotation.get("start"))
                    end_position = int(annotation.get("end"))      
                    entities.append((start_position, end_position, categories_spacy[0]))            

                if category == categories_sem_clin[1]:
                    start_position = int(annotation.get("start"))
                    end_position = int(annotation.get("end"))
                    entities.append((start_position, end_position, categories_spacy[1]))

                if category == categories_sem_clin[2]:
                    start_position = int(annotation.get("start"))
                    end_position = int(annotation.get("end"))
                    entities.append((start_position, end_position, categories_spacy[2]))

                if category == categories_sem_clin[3]:
                    start_position = int(annotation.get("start"))
                    end_position = int(annotation.get("end"))
                    entities.append((start_position, end_position, categories_spacy[3]))

                if category == categories_sem_clin[4]:
                    start_position = int(annotation.get("start"))
                    end_position = int(annotation.get("end"))
                    entities.append((start_position, end_position, categories_spacy[4]))

                if category == categories_sem_clin[5]:
                    start_position = int(annotation.get("start"))
                    end_position = int(annotation.get("end"))
                    entities.append((start_position, end_position, categories_spacy[5]))            

                if category == categories_sem_clin[6]:
                    start_position = int(annotation.get("start"))
                    end_position = int(annotation.get("end"))
                    entities.append((start_position, end_position, categories_spacy[6]))

                if category == categories_sem_clin[7]:
                    start_position = int(annotation.get("start"))
                    end_position = int(annotation.get("end"))
                    entities.append((start_position, end_position, categories_spacy[7]))

                if category == categories_sem_clin[8]:
                    start_position = int(annotation.get("start"))
                    end_position = int(annotation.get("end"))
                    entities.append((start_position, end_position, categories_spacy[8]))

                if category == categories_sem_clin[9]:
                    start_position = int(annotation.get("start"))
                    end_position = int(annotation.get("end"))
                    entities.append((start_position, end_position, categories_spacy[9]))

                if category == categories_sem_clin[10]:
                    start_position = int(annotation.get("start"))
                    end_position = int(annotation.get("end"))
                    entities.append((start_position, end_position, categories_spacy[10]))

                if category == categories_sem_clin[11]:
                    start_position = int(annotation.get("start"))
                    end_position = int(annotation.get("end"))
                    entities.append((start_position, end_position, categories_spacy[11]))

                if category == categories_sem_clin[12]:
                    start_position = int(annotation.get("start"))
                    end_position = int(annotation.get("end"))
                    entities.append((start_position, end_position, categories_spacy[12]))

                if category == categories_sem_clin[13]:
                    start_position = int(annotation.get("start"))
                    end_position = int(annotation.get("end"))
                    entities.append((start_position, end_position, categories_spacy[13]))

                if category == categories_sem_clin[14]:
                    start_position = int(annotation.get("start"))
                    end_position = int(annotation.get("end"))
                    entities.append((start_position, end_position, categories_spacy[14]))

                if category == categories_sem_clin[15]:
                    start_position = int(annotation.get("start"))
                    end_position = int(annotation.get("end"))
                    entities.append((start_position, end_position, categories_spacy[15]))

                if category == categories_sem_clin[16]:
                    start_position = int(annotation.get("start"))
                    end_position = int(annotation.get("end"))
                    entities.append((start_position, end_position, categories_spacy[16]))

        # monta a estrutura final aceita pelo spaCy
        output = (clinical_report_content, {"entities": entities})
        output_str = str(output)

        output_file_name = f"case{os.path.splitext(filename)[0]}.txt"
        output_file_path = os.path.join(output_dir, output_file_name)

        with open(output_file_path, "w", encoding="utf-8") as output_file:
            output_file.write(output_str)

        print(f"Output salvo em: {output_file_path}")