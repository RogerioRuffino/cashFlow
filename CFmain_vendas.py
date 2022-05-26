# -*- coding: utf-8 -*-
"""
Created on Sat May 21 15:26:34 2022

@author: Windows 11
"""
import sys
sys.path.append('C:/Users/Windows 11/OneDrive/Rogerio/rogerPythonTkinterApps/CashFlow')

def print_dc_vendas(dc_vendas,m):
    d= dc_vendas                      
    import pandas as pd   
    print (3*'\n')
    print(m*'_')
    print ('{:^40}'.format('Tabela de custos variaveis mensais'))
    print(m*'_')
    '____________________________________________________'
    'Inserir Header no dicionario na posicao 0'
    '----------------------------------------------------'
    l = ['tipo de', 'qtde de', 'valor R$']
    l1= ['animais', 'animais', 'do lote ']
    l2= ['-------', '-------', '--------']
    lval = list(d.values())
    lval.insert(0,l)
    lval.insert(1,l1)
    lval.insert(2,l2)
    lkey = list(d.keys())
    lkey.insert(0,'tipo animais')
    lkey.insert(1,'               ')
    lkey.insert(2,'---------------')
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
b = ("dc_vendas.json")
x = a + b
arq_exists(x)
print('concatenacao  ', x, "r ",r, '\n')

if r==0:
    '____________________r == 0: #arquivo NAO existe_______________________'
    from CFvendas import * #adiciona precos nos dc_vendas
    
    x = revenues()
    x.entradas(45)
    dc_vendas = x.dc_vendas
    x.print_dc_vendas(45)
    
    '@@@@@@@@@@@@@@@@@__Save dc_vendas___@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
    dc_vendas = x.dc_vendas
    import json
    #dc_vendas = {'milho': [2.0, 2.0, 1.0], 'nucleo': [2.0, 2.0, 1.0], 'silo': [2.0, 1000, 0.0], 'ração': [2.0, 2.0, 1.0], 'bicarbonato': [2.0, 2.0, 1.0], 'sal_mineral': [2.0, 2.0, 1.0], 'arroba_boi': [2.0, 2.0, 0]}
    dc_vendas = json.dumps(dc_vendas,  indent=True)
    with open ("dc_vendas.json", 'w+') as file:
        file.write(dc_vendas)
    '@@@@@@@@@@@@@@@@@__Fim Save dc_vendas___@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
    #print('dc_vendas apos save', dc_vendas)   
    print('____________________fim Class CFmercadorias____________________')

elif r==1:
    '_________r == 1: #arquivo dc_vendas existe______'
    
    '@@@@@@@@@@@@@@@@@@@@@@@@@@@ Read Arquivo @@@@@@@@@@@@@@@@@@@@@@@@@@@'
    import json
    with open('dc_vendas.json', 'r+') as file:
        dc_vendas = file.read()
        dc_vendas = json.loads(dc_vendas)
    
        #print('______________________________________________')
        #print('dc_vendas: ', dc_vendas, '\n')
        #print('______________________________________________')
    
    '@@@@@@@@@@@@_____Fim Leitura e print arquivo lido______@@@@@@@@@@@@@'
            
    print('')
    print(66*'=')
    print('dc_vendas: ', dc_vendas, '\n')
    print(66*'_')
    
    print(65*'=')
    print('====> Testa se preços dos dc_vendas estão atualizados_____________')
    print(65*'_')
    print_dc_vendas(dc_vendas, 45)
    
    entry = (input('Deseja atualizar digite s. Do contrário,  digite qualquer tecla: '))
    if entry == 's' or entry == 'S' :
        
        from CFvendas import *
        x = revenues()
        x.entradas(45)
        dc_vendas = x.dc_vendas
        x.print_dc_vendas(45)
        
        '@@@@@@@@@@@@@@@@@__Save dc_vendas___@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
        #dc_vendas = x.dc_vendas
        import json
        #dc_vendas = {'milho': [2.0, 2.0, 1.0], 'nucleo': [2.0, 2.0, 1.0], 'silo': [2.0, 1000, 0.0], 'ração': [2.0, 2.0, 1.0], 'bicarbonato': [2.0, 2.0, 1.0], 'sal_mineral': [2.0, 2.0, 1.0], 'arroba_boi': [2.0, 2.0, 0]}
        dc_vendas = json.dumps(dc_vendas,  indent=True)
        with open ("dc_vendas.json", 'w+') as file:
            file.write(dc_vendas)
        '@@@@@@@@@@@@@@@@@__Fim Save dc_vendas___@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
        #print('dc_vendas apos save', dc_vendas)
    
        print('proseeguir next Class')
        
       
print ('********************Fim***********************************')

