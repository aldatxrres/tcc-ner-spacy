# Extração de Informações em Relatos de Casos Clínicos com spaCy

Este repositório foi criado para realizar testes e treinamentos com a biblioteca **spaCy**, focando na extração de informações a partir de relatos de casos clínicos. Essa abordagem faz parte de uma pesquisa para o **Trabalho de Conclusão de Curso (TCC) de Sistemas de Informação** no IFES - Campus Cachoeiro de Itapemirim, pertencendo à Alda Torres. 

O objetivo é explorar como técnicas de Processamento de Linguagem Natural (PLN) podem ser aplicadas para automatizar a extração de dados em textos clínicos, contribuindo para o avanço das pesquisas na área de saúde.

## Funcionalidades
- Utilização do **spaCy** para identificar e extrair entidades nomeadas em textos médicos.
- Treinamento de modelos de reconhecimento de entidades nomeadas (NER).
- Análise de resultados e testes com diferentes configurações.

## Como Preparar o Ambiente

Siga os passos abaixo para configurar o ambiente de desenvolvimento e rodar os exemplos fornecidos:

### 1. Crie um Ambiente Virtual

No terminal, navegue até a pasta raiz do projeto e execute os comandos:

```bash
python -m venv venv
.\venv\Scripts\activate
```

Após ativar o ambiente virtual, o prompt de comando mostrará o nome do ambiente virtual entre parênteses (venv).

### 2. Instale as Dependências

Com o ambiente virtual ativado, execute:

```bash
pip install -U pip setuptools wheel
pip install -U spacy
python -m spacy download en_core_web_sm
```

Isso instalará o spaCy e o modelo de idioma necessário para processar textos em inglês.

### 3. Teste a Configuração
Para verificar se o spaCy foi configurado corretamente, execute:

```bash
python -m spacy info
```

### 4. Rodando um Teste Básico
Crie um arquivo teste.py e adicione o seguinte código:

```bash
import spacy

nlp = spacy.load("en_core_web_sm")

doc = nlp("Apple is looking at buying U.K. startup for $1 billion")

for ent in doc.ents:
    print(ent.text, ent.label_)
```

Esse código carrega o modelo de spaCy e realiza uma extração de entidades nomeadas (NER) de um exemplo simples.

### Possível Erro Comum
Se você encontrar o seguinte erro ao rodar o script:

```bash
OSError: [WinError 126] Não foi possível encontrar o módulo especificado. Error loading "caminho/para/seu/diretorio/Python/Python312/Lib/site-packages/torch/lib/fbgemm.dll" or one of its dependencies.
```

Isso indica que o interpretador pode estar usando a versão global do Python, e não a do ambiente virtual. Para forçar a execução com a versão correta do Python, utilize:

```bash
.\venv\Scripts\python.exe .\caminho\para\seu\arquivo\teste.py
```