# -*- coding: utf-8 -*-
"""
Created on Thu May 12 10:48:59 2022

@author: Windows 11
"""
import sys
sys.path.append('C:/Users/Windows 11/OneDrive/Rogerio/rogerPythonTkinterApps/CashFlow')

def print_dc_var(dc_var, m):
                          
    import pandas as pd   
    print (4*'\n')
    print(m*'_')
    print ('{:^40}'.format('Tabela de custos variaveis mensais'))
    print(m*'=')
    '____________________________________________________'
    'Inserir Header no dicionario na posicao 0'
    '----------------------------------------------------'
    l = ['consumo/','R$/Un','animais/','custos/']
    l1= ['cabeça  ','     ','lote    ','produto']
    l2= ['--------','-----','--------','-------']
    lval = list(dc_var.values())
    lval.insert(0,l)
    lval.insert(1,l1)
    lval.insert(2,l2)
    lkey = list(dc_var.keys())
    lkey.insert(0,'tipo de produto')
    lkey.insert(1,'               ')
    lkey.insert(2,'---------------')
    dc_var = dict(zip(lkey, lval))
    '----------------------------------------------------'
    df = pd.DataFrame(dc_var)
           
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
b = ("dc_var.json")
x = a + b
arq_exists(x)
print('concatenacao  ', x, "r ",r, '\n')

if r==0:
    '____________________r == 0: #arquivo NAO existe_______________________'
    from CFcustos_variaveis import * #adiciona precos nos dc_var
    
    x = var_costs([],{})
    x.entradas_var(55)
    dc_var = x.dc_var
    x.check_cVarMT()
    x.print_dc_var(55)
    #print('Custos Totais Variaveis',25*' ', x.cmt_cvar)
    
    '@@@@@@@@@@@@@@@@@__Save dc_var___@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
    dc_var = x.dc_var
    import json
    #dc_var = {'milho': [2.0, 2.0, 1.0], 'nucleo': [2.0, 2.0, 1.0], 'silo': [2.0, 1000, 0.0], 'ração': [2.0, 2.0, 1.0], 'bicarbonato': [2.0, 2.0, 1.0], 'sal_mineral': [2.0, 2.0, 1.0], 'arroba_boi': [2.0, 2.0, 0]}
    dc_var = json.dumps(dc_var,  indent=True)
    with open ("dc_var.json", 'w+') as file:
        file.write(dc_var)
    '@@@@@@@@@@@@@@@@@__Fim Save dc_var___@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
    print('dc_var apos save', dc_var)   
    print('____________________fim Class CFmercadorias____________________')

elif r==1:
    '_________r == 1: #arquivo dc_var existe______'
    
    '@@@@@@@@@@@@@@@@@@@@@@@@@@@ Read Arquivo @@@@@@@@@@@@@@@@@@@@@@@@@@@'
    import json
    with open('dc_var.json', 'r+') as file:
        dc_var = file.read()
        dc_var = json.loads(dc_var)
    
        #print('______________________________________________')
        #print('dc_var: ', dc_var, '\n')
        #print('______________________________________________')
    
    '@@@@@@@@@@@@_____Fim Leitura e print arquivo lido______@@@@@@@@@@@@@'
            
    print('')
    print(66*'=')
    print('dc_var: ', dc_var, '\n')
    print(66*'_')
    
    print(65*'=')
    print('====> Testa se preços dos dc_var estão atualizados_____________')
    print(65*'_')
    print_dc_var(dc_var, 58)
    
    entry = (input('Deseja atualizar digite s. Do contrário,  digite qualquer tecla: '))
    if entry == 's' or entry == 'S' :
        
        from CFcustos_variaveis import * #adiciona precos nos dc_var
        
        x = var_costs([],{})
        x.entradas_var(45)
        dc_var = x.dc_var
        print(' ate aki tem q ta certo' , dc_var)
        #x.check_cVarMT()
        x.print_dc_var(45)
        #print('Custos Totais Variaveis',25*' ', x.cmt_cvar)        
                
        #print('aki abestado', x.cmt_cvar) 
        
        '@@@@@@@@@@@@@@@@@__Save dc_var___@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
        dc_var = x.dc_var
        import json
        #dc_var = {'milho': [2.0, 2.0, 1.0], 'nucleo': [2.0, 2.0, 1.0], 'silo': [2.0, 1000, 0.0], 'ração': [2.0, 2.0, 1.0], 'bicarbonato': [2.0, 2.0, 1.0], 'sal_mineral': [2.0, 2.0, 1.0], 'arroba_boi': [2.0, 2.0, 0]}
        dc_var = json.dumps(dc_var,  indent=True)
        with open ("dc_var.json", 'w+') as file:
            file.write(dc_var)
        '@@@@@@@@@@@@@@@@@__Fim Save dc_var___@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
        print('dc_var apos save', dc_var)
    
        print('proseeguir next Class')
        
        
print ('********************Fim***********************************')

