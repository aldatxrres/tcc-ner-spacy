from bs4 import BeautifulSoup 
import os 

with open("extract-annotation-from-files-SemClinBr\\8907.xml", "r", encoding="UTF-8") as file: 
    xml = file.read()

soup = BeautifulSoup(xml, 'xml')

# extrai o conteúdo do relato de caso
clinical_report_content = soup.find("TEXT").text

# cria lista para receber futuras entidades
entities = []

# extrai as entidades do arquivo XML e atribui a sua variável correspondente
for tags in soup.find_all("TAGS"):
    for annotation in tags.find_all("annotation"):
        category = annotation.get("tag")
        start_position = annotation.get("start")
        end_position = annotation.get("end")

        # adiciona as entidades extraídas à lista de entidades
        entities.append((start_position, end_position, category))

# cria a saída no formato esperado pelo spaCy
output_annotation = (f"{clinical_report_content}", {"entities": [(entities)]})
print(output_annotation)

output_str = str(output_annotation)
output_dir = "annoted-clinical-reports"
output_file_path = os.path.join(output_dir, "case21.txt")

with open(output_file_path, "w", encoding="utf-8") as output_file:
    output_file.write(output_str)

print(f"\nOutput salvo em: {output_file_path}")