import os
from bs4 import BeautifulSoup

# Diretório onde estão os arquivos XML
input_dir = "files-SemClinBr"
output_dir = "annoted-clinical-reports"

# Cria o diretório de saída se ele não existir
os.makedirs(output_dir, exist_ok=True)

# Itera sobre todos os arquivos no diretório de entrada
for filename in os.listdir(input_dir):
    if filename.endswith(".xml"):
        input_file_path = os.path.join(input_dir, filename)
        
        # Lê o arquivo XML com o encoding UTF-8
        with open(input_file_path, "r", encoding="utf-8") as file:
            xml = file.read()

        # Analisa o conteúdo do XML
        soup = BeautifulSoup(xml, 'xml')

        # Extrai o conteúdo principal do relato de caso
        clinical_report_content = soup.find("TEXT").text

        # Lista para armazenar as entidades
        entities = []

        # Itera sobre todas as anotações e extrai as informações
        for tags in soup.find_all("TAGS"):
            for annotation in tags.find_all("annotation"):
                category = annotation.get("tag")
                start_position = int(annotation.get("start"))
                end_position = int(annotation.get("end"))
                
                # Adiciona a entidade à lista
                entities.append((start_position, end_position, category))

        # Monta a estrutura final
        output = (clinical_report_content, {"entities": entities})

        # Converte o output em uma string
        output_str = str(output)

        # Nome do arquivo de saída
        output_file_name = f"case{os.path.splitext(filename)[0]}.txt"
        output_file_path = os.path.join(output_dir, output_file_name)

        # Salva o output como um arquivo .txt com encoding UTF-8
        with open(output_file_path, "w", encoding="utf-8") as output_file:
            output_file.write(output_str)

        print(f"Output salvo em: {output_file_path}")