# Card Reader • Azure AI Document Intelligence

Aplicativo em **Streamlit** que lê a imagem de um cartão, extrai texto com **Azure AI Document Intelligence (prebuilt-read)** e exibe número mascarado, nome, validade, bandeira e validação Luhn.

## Funcionalidades
- Upload de imagem (PNG/JPG/JPEG)  
- Extração de texto via **prebuilt-read**  
- Detecção de número, nome e validade  
- Identificação da bandeira (Visa, Mastercard, Amex, etc)  
- Validação Luhn do número  
- Exibição mascarada do cartão  

## Pré-requisitos
- Python 3.9+  
- Recurso do [Azure AI Document Intelligence](https://learn.microsoft.com/azure/ai-services/document-intelligence/overview)  
- Endpoint e chave configurados nas variáveis de ambiente  

## Instalação
```bash
pip install -r requirements.txt
```

## Configuração de ambiente
```bash
export AZURE_DI_ENDPOINT=\"https://<seu-endpoint>.cognitiveservices.azure.com/\"
export AZURE_DI_KEY=\"<sua-chave>\"
```

## Uso
```bash
streamlit run app.py
```

Abra o navegador em `http://localhost:8501`, envie a imagem do cartão e visualize os dados extraídos.

## Estrutura do Projeto
```
.
├── app.py
├── services/
│   ├── azure_di.py
│   ├── parser.py
│   ├── validator.py
│   └── utils.py
└── requirements.txt
```