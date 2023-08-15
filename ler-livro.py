import PyPDF2 as ler
import pandas as pd
import re


def excluir_palavras(texto, palavras):
    for palavra in palavras:
        texto = texto.replace(palavra, '')
    return texto


pdf_file = open(r"C:\\Users\\nah26\\Downloads\\fonte.pdf", 'rb')
dados_pdf = ler.PdfReader(pdf_file)

indice1 = dados_pdf.pages[3]
indice2 = dados_pdf.pages[4]

conteudo_indice1 = indice1.extract_text()
conteudo_indice2 = indice2.extract_text()

palavras_exclusao = (
'I-TableofContents', 'TableofContents', 'Credits III', 'Introduction 1', 'TableofContents-II', 'AppendixA:',
'AppendixB:', 'AppendixC:HirelingCosts', 'AppendixD:', 'AppendixE:Conditions')

conteudo_indice1 = excluir_palavras(conteudo_indice1, palavras_exclusao)
conteudo_indice2 = excluir_palavras(conteudo_indice2, palavras_exclusao)

pattern = r"([A-Za-z\s]+)(\d+)"
matches_indice1 = re.findall(pattern, conteudo_indice1)
matches_indice2 = re.findall(pattern, conteudo_indice2)

criaturas = [{'Nome': match[0].strip(), 'Pagina': match[1]} for match in matches_indice1 + matches_indice2 if
             match[0].strip()]

df = pd.DataFrame(criaturas)

ambiente_paginas = {}

for index, row in df.iterrows():
    pagina = int(row['Pagina'])
    pagina_texto = dados_pdf.pages[pagina - 1].extract_text()

    # Encontrar o ambiente
    ambiente_match = re.search(r"Environment\s*:\s*(\w+)", pagina_texto)
    if ambiente_match:
        ambiente = ambiente_match.group(1)
    else:
        ambiente = 'Any'

    # Encontrar as tags
    tags_match = re.search(r"Tags\s*:\s*(.+)", pagina_texto)
    if tags_match:
        tags = tags_match.group(1)
    else:
        tags = ''

    # Adicionar ao dicionário
    if ambiente not in ambiente_paginas:
        ambiente_paginas[ambiente] = []

    ambiente_paginas[ambiente].append({'Nome': row['Nome'], 'Pagina': row['Pagina'], 'Tags': tags})

# Print do dicionário
for ambiente, criaturas in ambiente_paginas.items():
    print(f"Ambiente: {ambiente}")
    print(pd.DataFrame(criaturas).to_string())
    print("=" * 50)