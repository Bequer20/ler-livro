import PyPDF2 as ler
import pandas as pd

def remover_palavras(texto, palavras):
    for palavra in palavras:
        texto = texto.replace(palavra, '')
    return texto

def extrair_linhas(texto):
    linhas = texto.strip().split('\n')
    linhas_limpas = []
    for linha in linhas:
        if linha.strip():
            linhas_limpas.append(linha.strip())
    return linhas_limpas

pdf_file = open(r"C:\\Users\\nah26\\Downloads\\fonte.pdf", 'rb')
dados_pdf = ler.PdfReader(pdf_file)

total_pag = len(dados_pdf.pages)
print(f"Total de páginas: {total_pag}")

indice1 = dados_pdf.pages[3]
indice2 = dados_pdf.pages[4]

conteudo_indice1 = indice1.extract_text()
conteudo_indice2 = indice2.extract_text()

palavras = ('I-TableofContents', 'TableofContents', 'Credits III', 'Introduction 1', 'TableofContents-II','AppendixA:','AppendixB:','AppendixC:HirelingCosts','AppendixD:','AppendixE:Conditions')
conteudo_indice1 = remover_palavras(conteudo_indice1, palavras)
conteudo_indice2 = remover_palavras(conteudo_indice2, palavras)

def criar_dataframe(conteudo):
    linhas = extrair_linhas(conteudo)
    criaturas = []

    for linha in linhas:
        partes = linha.split()
        if len(partes) >= 2:
            nome = ' '.join(partes[:-1])
            pagina = partes[-1]
            criaturas.append({'Nome': nome, 'Pagina': pagina})

    return pd.DataFrame(criaturas)

df1 = criar_dataframe(conteudo_indice1)
df2 = criar_dataframe(conteudo_indice2)

df = pd.concat([df1, df2], ignore_index=True)

print(df.to_string())
