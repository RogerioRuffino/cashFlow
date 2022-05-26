# -*- coding: utf-8 -*-
"""
Created on Wed May 11 16:11:26 2022

@author: Windows 11
"""

import sys
sys.path.append('C:/Users/Windows 11/OneDrive/Rogerio/rogerPythonTkinterApps/CashFlow')




def print_dc_fixos(dc_fixos, m):
    d= dc_fixos                      
    import pandas as pd   
    print (3*'\n')
    print(m*'_')
    print ('{:^40}'.format('Tabela de custos variaveis mensais'))
    print(m*'=')
    
    '____________________________________________________'
    'Inserir Header no dicionario na posicao 0'
    '----------------------------------------------------'
    l = ['R$ por mês']
    l1= ['da despesa']
    l2= ['----------']
    lval = list(d.values())
    lval.insert(0,l)
    lval.insert(1,l1)
    lval.insert(2,l2)
    lkey = list(d.keys())
    lkey.insert(0,'tipo de')
    lkey.insert(1,'custo  ')
    lkey.insert(2,'-------')
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
b = ("dc_fixos.json")
x = a + b
arq_exists(x)
print('concatenacao  ', x, "r ",r, '\n')

if r==0:
    '____________________r == 0: #arquivo NAO existe_______________________'
    from CFcustos_fixos import * #adiciona precos nos dc_fixos
    
    x = fixed_cost()
    x.entradas()
    dc_fixos=x.dc_fixos
    #x.check_cFixMT()
    x.print_dc_fixos(35)  
    
    '@@@@@@@@@@@@@@@@@__Save dc_fixos___@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
    dc_fixos = x.dc_fixos
    import json
    #dc_fixos = {'milho': [2.0, 2.0, 1.0], 'nucleo': [2.0, 2.0, 1.0], 'silo': [2.0, 1000, 0.0], 'ração': [2.0, 2.0, 1.0], 'bicarbonato': [2.0, 2.0, 1.0], 'sal_mineral': [2.0, 2.0, 1.0], 'arroba_boi': [2.0, 2.0, 0]}
    dc_fixos = json.dumps(dc_fixos,  indent=True)
    with open ("dc_fixos.json", 'w+') as file:
        file.write(dc_fixos)
    '@@@@@@@@@@@@@@@@@__Fim Save dc_fixos___@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
    #print('dc_fixos apos save', dc_fixos)   
    print('____________________fim Class CFmercadorias____________________')

elif r==1:
    '_________r == 1: #arquivo dc_fixos existe______'
    
    '@@@@@@@@@@@@@@@@@@@@@@@@@@@ Read Arquivo @@@@@@@@@@@@@@@@@@@@@@@@@@@'
    import json
    with open('dc_fixos.json', 'r+') as file:
        dc_fixos = file.read()
        dc_fixos = json.loads(dc_fixos)
    
        #print('______________________________________________')
        #print('dc_fixos: ', dc_fixos, '\n')
        #print('______________________________________________')
    
    '@@@@@@@@@@@@_____Fim Leitura e print arquivo lido______@@@@@@@@@@@@@'
            
    print('')
    print(66*'=')
    print('dc_fixos: ', dc_fixos, '\n')
    print(66*'_')
    
    print(65*'=')
    print('====> Testa se preços dos dc_fixos estão atualizados_____________')
    print(65*'_')
    print_dc_fixos(dc_fixos, 45)
    
    entry = (input('Deseja atualizar digite s. Do contrário,  digite qualquer tecla: '))
    if entry == 's' or entry == 'S' :
        
        from CFcustos_fixos import *
        x = fixed_cost()
        x.entradas()
        dc_fixos=x.dc_fixos
        #x.check_cFixMT()
        x.print_dc_fixos(35)  
    
        '@@@@@@@@@@@@@@@@@__Save dc_fixos___@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
        dc_fixos = x.dc_fixos
        import json
        #dc_fixos = {'milho': [2.0, 2.0, 1.0], 'nucleo': [2.0, 2.0, 1.0], 'silo': [2.0, 1000, 0.0], 'ração': [2.0, 2.0, 1.0], 'bicarbonato': [2.0, 2.0, 1.0], 'sal_mineral': [2.0, 2.0, 1.0], 'arroba_boi': [2.0, 2.0, 0]}
        dc_fixos = json.dumps(dc_fixos,  indent=True)
        with open ("dc_fixos.json", 'w+') as file:
            file.write(dc_fixos)
        '@@@@@@@@@@@@@@@@@__Fim Save dc_fixos___@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
        #print('dc_fixos apos save', dc_fixos)
    
        print('proseeguir next Class')
        
        
print ('********************Fim***********************************')
