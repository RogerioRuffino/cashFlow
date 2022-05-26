# -*- coding: utf-8 -*-
"""
Created on Wed May 18 15:17:06 2022

@author: Windows 11
"""
class revenues():
    def __init__(self, dc_vendas = {}, d={}, lc_vendas=[], l=[]):
        
        self.lc_vendas = lc_vendas
        self.dc_vendas = dc_vendas
        self.d = d
 


    def check_string(self,  texto):
        
        global a
        while True:
          try:
               a = str(input("Digite %s: "%(texto)))
               if a.isascii(): 
                  break
               raise ValueError                                      
          except ValueError:
               print('Entrada invalida digite de novo')
        return a
   
    def check_float(self,  texto):
        
        global a
        while True:
          try:
             a = float(input("Digite o %s: "%(texto)))
             if a <= 0 or a is  str: 
                raise ValueError
             break                                                     
          except ValueError:
               print('Entrada invalida digite de novo')
        return a
    
    def check_soma(self, d):
        
        a=0
        print('bestalhao ', d)
        for key in d.keys():
            #print(d[key])
            a += d[key][2]
        return a

    def entradas(self, m):    
        b=0
        keys=[]
        values=[]
        
        texto = '''
Digite s se tem animais vendidos ou,
Digite qualquer tecla, caso não tenha==> '''
        while True:
            b = input((texto))
            if b=='s':
                               
                print(m*'=')
                print('{:^40}'.format('animais vendidos '))
                print(m*'_')
                tan =  revenues().check_string("o tipo de animal vendido")
                keys.append(tan)
                
                qan = revenues().check_float(' quantidade de animais')
                van = revenues().check_float(' valor por cabeça')
    
                l = [qan, van , qan*van]
                values.append(l)
            
            elif b!='s':
                break
            texto = "se ha mais custos digite s, ou qq tecla se não há==> "
            
        ll=[]   
        #keys.append('custos fixos totais')
        #ll=[check_soma(self, d) ]
        print(keys, '\n', values)
        lc_vendas = values
        d = dict(zip(keys, values))
        print('d ', self.d,'\n')
        print(20*'=')
    
        soma = revenues().check_soma(d)
        print('abestado ====> ', soma)
        print(20*'_')
        
        l = ['-', '-', soma]
        values.append(l)
        keys.append('receitas totais')
        print('keys  ', keys, 'values', values)
        self.lc_vendas = values
        self.dc_vendas = dict(zip(keys, values))
        print('==========================')
        print('lista de lc_vendas', self.lc_vendas, '\n')
        
        print('dicionario de dc_vendas ', self.dc_vendas)
    
    def print_dc_vendas(self, m):
        d= self.dc_vendas                      
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


    
'''        
x = revenues()
x.entradas(45)
dc_vendas = x.dc_vendas
x.print_dc_vendas(45)
'''

