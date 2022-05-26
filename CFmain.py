# -*- coding: utf-8 -*-
"""
Created on Sat May 21 17:58:18 2022

@author: Windows 11
"""
def plot_cash_flow(d,m):
    import pandas as pd   
    print (3*'\n')
    print(m*'_')
    print ('{:^40}'.format('Tabela Resultados Mensais'))
    print(m*'=')
    df = pd.DataFrame(d)
    df.plot.bar(title = 'cash flow mensal', color = ['b', 'r', 'g'])
    #print(df)
    
def print_cash_flow(d, m):
                          
    import pandas as pd   
    print (3*'\n')
    print(m*'_')
    print ('{:^40}'.format('Tabela Resultados Mensais'))
    print(m*'=')
    '____________________________________________________'
    'Inserir Header no dicionario na posicao 0'
    '----------------------------------------------------'
    l = ['R$ no']
    l1= ['mês  ']
    l2= ['----------']
    lval = list(d.values())
    lval.insert(0,l)
    lval.insert(1,l1)
    lval.insert(2,l2)
    lkey = list(d.keys())
    lkey.insert(0,'resultados')
    lkey.insert(1,'no mês ')
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

from CFmain_Mercadorias import *

'''import json
with open('produtos.json', 'r+') as file:
    produtos = file.read()
    produtos = json.loads(produtos)
    print(3*"\n")'''
print(47*'=')
print('ai bestalhao ', produtos)
print(47*'=')
print('_________________________________________________')
 
from CFmain_custos_variaveis import *

'''import json
with open('dc_var.json', 'r+') as file:
    dc_var = file.read()
    dc_var = json.loads(dc_var)
    print(3*"\n")
    '''
print(47*'=')
print('ai bestalhao ', dc_var)
print(47*'=')
print('_________________________________________________')

from CFmain_custos_fixos import *

'''
import json
with open('dc_fixos.json', 'r+') as file:
    dc_fixos = file.read()
    dc_fixos = json.loads(dc_fixos)
    print(3*"\n")
    '''
print(47*'=')
print('ai bestalhao ', dc_fixos)
print(47*'=')
print('_________________________________________________')

from CFmain_vendas import *

print(47*'=')
print('ai bestalhao ', dc_vendas)
print(47*'=')
print('_________________________________________________')

from CFmain_dataMilk import *

print(47*'=')
print('dc_milk ', dc_milk)
print(47*'=')
print('_________________________________________________')

m=47
print(10*'\n')
print(47*'+')
print('dc_var   ', dc_var,'\n')
print('dc_fixos  ', dc_fixos,'\n')
print('dc_vendas ', dc_vendas,'\n')
print('dc_milk ', dc_milk,'\n')
print(47*'+')
d = {}
print (3*'\n')
print('====================================================')
print ('{:^40}'.format('receita do leite'))
print('____________________________________________________')
rvl = dc_milk['receita em R$/mes'][0]
rva = dc_vendas['receitas totais'][2]
srm = rvl+rva
d['receitas totais no mês'] = [srm]
print('receitas totais no mês ', d)
print('====================================================')


print('')
print('====================================================')
print ('{:^40}'.format('custos totais mês'))
print('____________________________________________________')
cvt = dc_var['Custos Totais Variaveis'][3]
cft = dc_fixos['custos fixos totais']
scm =-cvt-cft
d['custos totais no mês'] = [scm]
print('custos totais no mês ', d)

print('====================================================')

print('')
print('====================================================')
print ('{:^40}'.format('cash flow no mês'))
print('____________________________________________________')
resultado_m = srm+scm
d['cash flow no mes'] = [resultado_m]
print('cash flow no mês ', d)
print('====================================================')


print_cash_flow(d, 35)
plot_cash_flow(d,35)




