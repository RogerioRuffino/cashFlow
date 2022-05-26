# -*- coding: utf-8 -*-
"""
Created on Sat May 21 16:51:52 2022

@author: Windows 11
"""
import sys
sys.path.append('C:/Users/Windows 11/OneDrive/Rogerio/rogerPythonTkinterApps/CashFlow')

def print_dc_milk(dc_milk, m):
    texto = "Dados da produçao de leite"                      
    import pandas as pd   
    d = dc_milk
    print (4*'\n')
    print(m*'_')
    print ('{:^33}'.format(texto))
    #print(m*'_')
    '____________________________________________________'
    'Inserir Header no dicionario na posicao 0'
    '----------------------------------------------------'
    l = ['=======']
    l1= ['Valores']
    l2= ['-------']
    lval = list(d.values())
    lval.insert(0,l)
    lval.insert(1,l1)
    lval.insert(2,l2)
    lkey = list(d.keys())
    lkey.insert(0,'==============')
    lkey.insert(1,'Dados do Leite')         
    lkey.insert(2,'--------------')
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
b = ("dc_milk.json")
x = a + b
arq_exists(x)
print('concatenacao  ', x, "r ",r, '\n')

if r==0:
    '____________________r == 0: #arquivo NAO existe_______________________'
    from CFdataMilk import * #adiciona precos nos dc_milk
    
    x = milk_data()   
    x.entradas()
    dc_milk = x.dc_milk
    x.print_dc_milk(33)
    
    '@@@@@@@@@@@@@@@@@__Save dc_milk___@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
    import json
    #dc_milk = {'milho': [2.0, 2.0, 1.0], 'nucleo': [2.0, 2.0, 1.0], 'silo': [2.0, 1000, 0.0], 'ração': [2.0, 2.0, 1.0], 'bicarbonato': [2.0, 2.0, 1.0], 'sal_mineral': [2.0, 2.0, 1.0], 'arroba_boi': [2.0, 2.0, 0]}
    dc_milk = json.dumps(dc_milk,  indent=True)
    with open ("dc_milk.json", 'w+') as file:
        file.write(dc_milk)
    '@@@@@@@@@@@@@@@@@__Fim Save dc_milk___@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
    #print('dc_milk apos save', dc_milk)   
    print('____________________fim Class CFmercadorias____________________')

elif r==1:
    '_________r == 1: #arquivo dc_milk existe______'
    
    '@@@@@@@@@@@@@@@@@@@@@@@@@@@ Read Arquivo @@@@@@@@@@@@@@@@@@@@@@@@@@@'
    import json
    with open('dc_milk.json', 'r+') as file:
        dc_milk = file.read()
        dc_milk = json.loads(dc_milk)
    
        #print('______________________________________________')
        #print('dc_milk: ', dc_milk, '\n')
        #print('______________________________________________')
    
    '@@@@@@@@@@@@_____Fim Leitura e print arquivo lido______@@@@@@@@@@@@@'
            
    print('')
    print(66*'=')
    print('dc_milk: ', dc_milk, '\n')
    print(66*'_')
    
    print(65*'=')
    print('====> Testa se preços dos dc_milk estão atualizados_____________')
    print(65*'_')
    print_dc_milk(dc_milk, 45)
    
    entry = (input('Deseja atualizar digite s. Do contrário,  digite qualquer tecla: '))
    if entry == 's' or entry == 'S' :
        
        from CFdataMilk import * #adiciona precos nos dc_milk
        
        x = milk_data()   
        x.entradas()
        dc_milk = x.dc_milk
        x.print_dc_milk(33)
        
        '@@@@@@@@@@@@@@@@@__Save dc_milk___@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
        dc_milk = x.dc_milk
        import json
        #dc_milk = {'milho': [2.0, 2.0, 1.0], 'nucleo': [2.0, 2.0, 1.0], 'silo': [2.0, 1000, 0.0], 'ração': [2.0, 2.0, 1.0], 'bicarbonato': [2.0, 2.0, 1.0], 'sal_mineral': [2.0, 2.0, 1.0], 'arroba_boi': [2.0, 2.0, 0]}
        dc_milk = json.dumps(dc_milk,  indent=True)
        with open ("dc_milk.json", 'w+') as file:
            file.write(dc_milk)
        '@@@@@@@@@@@@@@@@@__Fim Save dc_milk___@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
        #print('dc_milk apos save', dc_milk)
    
        print('proseeguir next Class')
        
        
print ('********************Fim***********************************')

