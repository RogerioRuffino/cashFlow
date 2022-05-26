
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 14:12:00 2022

@author: Windows 11
"""
import sys
sys.path.append('C:/Users/Windows 11/OneDrive/Rogerio/rogerPythonTkinterApps/CashFlow')

def print_produtos(produtos, m):
                              
    import pandas as pd
    d = produtos
    #print (2*'\n')
    print(m*'_')
    print ('{:^45}'.format('Tabela de produtos'))
    print(m*'=')
    
    '____________________________________________________'
    'Inserir Header no dicionario na posicao 0'
    '----------------------------------------------------'
    l = ['preço por', 'peso da', 'valor em  ']
    l1= ['saca     ', 'saca   ', ' R$ por kg']
    l2= ['---------', '---------', '------------']
    lval = list(d.values())
    lval.insert(0,l)
    lval.insert(1,l1)
    lval.insert(2,l2)
    lkey = list(d.keys())
    lkey.insert(0,'tipo de ')
    lkey.insert(1,'produto ')
    lkey.insert(2,'--------')
    d = dict(zip(lkey, lval))
    '----------------------------------------------------'
    df = pd.DataFrame(d)
           
    blankIndex=[''] * len(df)  #Tira a aprimeira coluna
    df.index=blankIndex
    #print(df)
        
    df_tr = df.transpose() #Inverte Linha x Coluna no Dataframe
    #print(df.to_markdown(index=False)) 
    print(df_tr)
    print(m*'_')

def arq_exists(x):
    import os
    global r
    file_path = (x)
    #file_path = ("C:/Users/Windows 11/OneDrive/Rogerio/rogerPythonTkinterApps/CashFlow/+texto")
    print(file_path)
    if not os.path.exists(file_path):
        r=0
        print('NAO existe seja arquivo ou diretorio')
    else: 
        r=1
        print('existe seja arquivo ou diretorio')
    return  r
print(26*'')
#a = ("C:/Users/Windows 11/OneDrive/Rogerio/rogerPythonTkinterApps/CashFlow/")
a=("") # nao usei o end completo pois ja informei no sys
b = ("produtos.json")
x = a + b
arq_exists(x)
print('concatenacao  ', x, "r ",r, '\n')

if r==0:
    '____________________r == 0: #arquivo NAO existe_______________________'
    from CFmercadorias import *
    x = entradas()
    x.valores(57)
    x.print_produtos(47)
    produtos=x.produtos
    print('conseguiu bestalhao ', x.produtos)

    '@@@@@@@@@@@@@@@@@__Save produtos___@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
    produtos = x.produtos
    import json
    #produtos = {'milho': [2.0, 2.0, 1.0], 'nucleo': [2.0, 2.0, 1.0], 'silo': [2.0, 1000, 0.0], 'ração': [2.0, 2.0, 1.0], 'bicarbonato': [2.0, 2.0, 1.0], 'sal_mineral': [2.0, 2.0, 1.0], 'arroba_boi': [2.0, 2.0, 0]}
    produtos = json.dumps(produtos,  indent=True)
    with open ("produtos.json", 'w+') as file:
        file.write(produtos)
    '@@@@@@@@@@@@@@@@@__Fim Save produtos___@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
    #print('produtos apos save', produtos)   
    print('____________________fim Class CFmercadorias____________________')

elif r==1:
    '_________r == 1: #arquivo produtos existe______'
    
    '@@@@@@@@@@@@@@@@@@@@@@@@@@@ Read Arquivo @@@@@@@@@@@@@@@@@@@@@@@@@@@'
    import json
    with open('produtos.json', 'r+') as file:
        produtos = file.read()
        produtos = json.loads(produtos)
    
        #print('______________________________________________')
        #print('produtos: ', produtos, '\n')
        #print('______________________________________________')
    
    '@@@@@@@@@@@@_____Fim Leitura e print arquivo lido______@@@@@@@@@@@@@'
            
    print('')
    print(66*'=')
    print('produtos: ', produtos, '\n')
    print(66*'_')
    
    print(65*'=')
    print('====> Testa se preços dos produtos estão atualizados_____________')
    print(65*'_')
    print_produtos(produtos, 47)
    
    entry = (input('Deseja atualizar digite s. Do contrário,  digite qualquer tecla: '))
    if entry == 's' or entry == 'S' :
        
        from CFmercadorias import *
        x = entradas()
        x.valores(57)
        x.print_produtos(47)
        produtos=x.produtos
        #print('conseguiu bestalhao ', x.produtos)
    
        '@@@@@@@@@@@@@@@@@__Save produtos___@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
        produtos = x.produtos
        import json
        #produtos = {'milho': [2.0, 2.0, 1.0], 'nucleo': [2.0, 2.0, 1.0], 'silo': [2.0, 1000, 0.0], 'ração': [2.0, 2.0, 1.0], 'bicarbonato': [2.0, 2.0, 1.0], 'sal_mineral': [2.0, 2.0, 1.0], 'arroba_boi': [2.0, 2.0, 0]}
        produtos = json.dumps(produtos,  indent=True)
        with open ("produtos.json", 'w+') as file:
            file.write(produtos)
        '@@@@@@@@@@@@@@@@@__Fim Save produtos___@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
        #print('produtos apos save', produtos)
    
        print('proseeguir next Class')
        print ('_______________Fim+++++++++++++++++++++++++++++++++++++++')
        
pass