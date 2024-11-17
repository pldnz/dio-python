# pip install requests beautifulsoup4 openai langchain-openai

import requests
from bs4 import BeautifulSoup
from langchain_openai.chat_models.azure import AzureChatOpenAI

def extrair_texto_da_pagina(url):
  response = requests.get(url)

  if response.status_code != 200:
    print(f"Erro ao acessar a página. Código de status: {response.status_code}")
    return None
  else:
    soup = BeautifulSoup(response.text, 'html.parser')
    for script_or_style in soup(["script", "style"]):
      script_or_style.decompose()
      texto = soup.get_text(separator= ' ')

      # limpando texto
      linhas = (line.strip() for line in texto.splitlines())
      parts = (phrase.strip() for line in linhas for phrase in line.split("  "))
      texto = '\n'.join(part for part in parts if part)
      return texto
    


client = AzureChatOpenAI(
    azure_endpoint="YOUR_AZURE_ENDPOINT",
    api_key="YOUR_AZURE_API_KEY",
    api_version="2024-02-15-preview",
    deployment_name="gpt-4o-mini",
    max_retries=0
)

def traduzir_artigo(text, lang):
  messages = [
      ("system", "Você atua como tradutor de textos"),
      ("human", f"Traduza o {text} para o diioma {lang} e responda em markdown")
  ]

  response = client.invoke(messages)
  return response.content


# traduzir_artigo("Hello friend", "portugues")
extrair_texto_da_pagina("https://dev.to/amananandrai/open-ai-starts-the-year-with-a-bang-5hbh")