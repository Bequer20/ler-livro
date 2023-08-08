import PyPDF2 as ler
import pandas as pd

def remover_palavras(texto, palavras):
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

palavras = ('I-TableofContents', 'TableofContents', 'Credits III', 'Introduction 1', 'TableofContents-II')
conteudo_indice1 = remover_palavras(conteudo_indice1, palavras)
conteudo_indice2 = remover_palavras(conteudo_indice2, palavras)
print(conteudo_indice1, conteudo_indice2)
criaturas1 = []
criaturas2 = []

linhas1 = conteudo_indice1.strip().split('\n')
linhas2 = conteudo_indice2.strip().split('\n')

for linha in linhas1:
    partes = linha.split()
    if len(partes) >= 2:
        nome = ' '.join(partes[:-1])
        pagina = partes[-1]
        criaturas1.append({'Nome': nome, 'Pagina': pagina})

for linha in linhas2:
    partes = linha.split()
    if len(partes) >= 2:
        nome = ' '.join(partes[:-1])
        pagina = partes[-1]
        criaturas2.append({'Nome': nome, 'Pagina': pagina})

df1 = pd.DataFrame(criaturas1)
df2 = pd.DataFrame(criaturas2)

df = pd.concat([df1, df2], ignore_index=True)


print(df)
