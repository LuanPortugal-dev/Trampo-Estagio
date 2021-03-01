import tabula
import os
import pandas as pd
import re
from tqdm.notebook import tqdm
from conexao import enviar_dados
#import bot


pdf_folder = 'C:/tabula/pdfs/'
paths = [pdf_folder + fn for fn in os.listdir(pdf_folder) if fn.endswith('.pdf')]




def dados(df):
    lista = df.columns.tolist()
    cases = []

    for i in lista:
         
        for z in df[i]:
            #if "CPF" in z:
            if re.search(r'(\d\d\d.\d\d\d.\d\d\d-\d\d)', str(z)):
                cpf = str(z).split()[-1].replace('.', '').replace('-', '')
             


            if "(" in str(z) and ")" in str(z) and "-" in str(z) and "Telefone" not in str(z) and re.search(r'(\d)', str(z)): 
                telefone = str(z)[:17].replace('(', '').replace(')', '').replace('-', '').replace(' ','')
               
            

            if "(" in str(z) and ")" in str(z) and "-" in str(z) and "Telefone" not in str(z) and re.search(r'(\d)', str(z)): 
                celular = str(z)[18:34].replace('(', '').replace(')', '').replace('-', '').replace(' ','')
             


            if "@" in str(z):
                email = z.split()[-1].islower()
            


        for i in df[:3].values.tolist():
            for z in i:
                if str(z).isupper():          
                    cases.append(z)
                    nome = cases[0]
                  

    enviar_dados(nome, cpf, email, telefone)     


for path in tqdm(paths):
    list_df = tabula.read_pdf(path, encoding = 'latin1', pages= "all")
    df = pd.concat([list_df[0], list_df[1]])

    dados(df)
    
