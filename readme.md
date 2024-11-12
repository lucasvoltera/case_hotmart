## Case Hotmart

Este projeto foi feito para o case técnico da hotmart, onde o objetivo foi criar microserviços que extraem textos de uma url, faz os processamentos necessários e manda-os para um banco de dados vetorial. Em seguida, usa-se esse banco de dados para fazer um RAG e gerar respostas mais precisas.

## Arquitetura do Projeto

O projeto é dividido em dois microsserviços principais:

### 1. service_etl (Processamento e Armazenamento de Documentos)

Este microsserviço é responsável por:

    Receber um documento de texto de uma URL.
    Realizar o scraping da página para extrair os trechos de texto.
    Processar e armazenar esses trechos em um Vector Database.


### 2. service_rag (Busca e Resposta com LLM)

Este microsserviço é responsável por:

    Receber uma pergunta em formato de texto.
    Consultar o Vector Database para buscar os trechos mais relevantes que correspondem ao contexto da pergunta.
    Usar esses trechos como contexto de entrada para uma LLM e gerar uma resposta.


## Estrutura do Projeto


```
├── docker-compose.yml
├── service_etl
│   ├── app.py
│   ├── config.py
│   ├── database.py
│   ├── Dockerfile
│   ├── models.py
│   ├── utils.py
│   ├── vectorization.py
│   ├── scraper.py
│   ├── requirements.txt
│   └── test.http
└── service_rag
    ├── app.py
    ├── ai_client.py
    ├── config.py
    ├── database.py
    ├── requirements.txt
    └── test.http

```

1. `service_etl` - Processamento e Armazenamento de Documentos

    * app.py: Lógica principal da API.
    * config.py: Configurações gerais (variáveis de ambiente, URLs).
    * database.py: Interações com o banco de dados vetorial.
    * Dockerfile: Configuração para a imagem Docker.
    * models.py: Modelos de dados (ex.: URLRequest).
    * utils.py: Funções auxiliares (hash, validação).
    * vectorization.py: Vetorização do texto em embeddings.
    * scraper.py: Scraping e extração de conteúdo.
    * requirements.txt: Dependências do projeto.
    * test.http: Exemplos de requisições para teste da API.

2. `service_rag` - Busca e Resposta com LLM

    * app.py: Lógica principal da API.
    * ai_client.py: Integração com a LLM para geração de respostas.
    * config.py: Configurações gerais (variáveis de ambiente, URLs).
    * database.py: Interações com o banco de dados vetorial para busca de trechos relevantes.
    * requirements.txt: Dependências do projeto.
    * test.http: Exemplos de requisições para teste da API.

## Tecnologias Utilizadas

* FastAPI: Framework para APIs RESTful, usado nos microsserviços.
* Qdrant: Banco de dados vetorial para armazenamento e busca de embeddings de texto.
* OpenAI GPT-4o-mini: Modelo usado para gerar respostas com base nos textos encontrados, escolhido pela * limitação de hardware para LLMs locais.
* Docker: Empacota os microsserviços em containers.
* Python 3.9: Linguagem principal do projeto.


## Como Rodar o Projeto

### Requisitos 
    
    * Docker
    * Extensão REST Client no VSCODE

### Passo a passo
1. Clone o repositório com git clone `https://github.com/lucasvoltera/case_hotmart.git`. 
2. Acesse o diretório do projeto com `cd case_hotmart`.
3. Em cada microsserviço (`service_etl` e `service_rag`), crie um arquivo .env com as variáveis de ambiente necessárias:
    ```
    OPENAI_API_KEY=your-openai-api-key
    QDRANT_URL=http://qdrant:6333
    ```
4. No diretório raiz do projeto, execute `docker-compose up --build` para construir e iniciar os serviços
5. Acesse a API `service_etl` para enviar o documento e criar o banco de dados vetorial.
6. Teste a API `service_rag` para realizar as consultas.

## Testando os Microsserviços

### Opção 1. Usando a extensão REST Client para executar arquivos .http
* `service_etl`:

    Faça alguma requisição no arquivo test.http

* `service_rag`:

    Faça alguma requisição no arquivo test.http.

### Opção 2. Curl
Para testar os microsserviços com curl, execute os comandos abaixo:
* `service_etl`:

```
curl -X POST http://localhost:8001/upload -H "Content-Type: application/json" -d "{\"url\": \"https://hotmart.com/pt-br/blog/como-funciona-hotmart\"}"
```

* `service_rag`
```
curl -X POST http://localhost:8002/ask -H "Content-Type: application/json" -d "{\"question\": \"Quanto a hotmart cobra por venda?\"}"
```
