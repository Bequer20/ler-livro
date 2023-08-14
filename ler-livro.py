import PyPDF2 as ler
import pandas as pd
import re

def excluir_palavras(texto, palavras):
    for palavra in palavras:
        texto = texto.replace(palavra, '')
    return texto

pdf_file = open(r"C:\\Users\\nah26\\Downloads\\fonte.pdf", 'rb')
dados_pdf = ler.PdfReader(pdf_file)

total_pag = len(dados_pdf.pages)
print(f"Total de páginas: {total_pag}")

indice1 = dados_pdf.pages[3]
indice2 = dados_pdf.pages[4]

conteudo_indice1 = indice1.extract_text()
conteudo_indice2 = indice2.extract_text()

palavras_exclusao = ('I-TableofContents', 'TableofContents', 'Credits III', 'Introduction 1', 'TableofContents-II','AppendixA:','AppendixB:','AppendixC:HirelingCosts','AppendixD:','AppendixE:Conditions')

conteudo_indice1 = excluir_palavras(conteudo_indice1, palavras_exclusao)
conteudo_indice2 = excluir_palavras(conteudo_indice2, palavras_exclusao)

pattern = r"([A-Za-z\s]+)(\d+)"
matches_indice1 = re.findall(pattern, conteudo_indice1)
matches_indice2 = re.findall(pattern, conteudo_indice2)

criaturas = [{'Nome': match[0].strip(), 'Pagina': match[1]} for match in matches_indice1 + matches_indice2 if match[0].strip()]

df = pd.DataFrame(criaturas)

print(df.to_string(index=False))
