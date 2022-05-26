# -*- coding: utf-8 -*-
"""
Created on Sun May  1 12:22:37 2022

@author: Windows 11
"""
'''
Gasolina #km x lt/km*R$/lt
Veterinario # mensal
Financiamento Trator  #anual
Financiamento Implementos #anual
Contador # mensal
Diesel #km x lt/km*R$/lt
Energia Eletrica # mensal
Func 1 # mensal
Func 2 # mensal
Func 3 # mensal
Func Limpeza # mensal
INSS Produtor # mensal
Manutencao # mensal
Modem Internet # mensal
Remedios # mensal
Seguros #anual
Seguro Vida #anual 
Serviços Bancarios # mensal
Telefone Faz # mensal
Plano Saude # mensal
Visa # mensal
'''
class fixed_cost():
    def __init__(self,  custos={}, valores={},
                 dc_fixos = {}, lc_fixos=[], l=[]):
        
        self.custos = custos
        self.valores = valores
        self.lc_fixos = lc_fixos
        self.dc_fixos = dc_fixos
    
    def check_string(self,  texto):
        
        global a
        while True:
          try:
               a = str(input("Digite o %s: "%(texto)))
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
    
    
    def check_cFixMT(self, d):
        
        global a
        self.cmt_cfix=0
        for key in d.keys():
            #print(d[key])
            a += d[key]
            
        return a
        
    def entradas(self):    
        
        keys=[]
        values=[]
        texto= 'digite s para iniciar==> '
        while True:
            b = input((texto))
            if b!='n':
                print(45*'-')
                k =  fixed_cost().check_string("nome da despesa mensal")
                keys.append(k)
                v = fixed_cost().check_float('valor da despesa mensal')
                values.append(v)
                print(45*'-')

            elif b=='n':
                break
            texto = '''
se há mais custos digite qq tecla, 
ou n se não há==> '''
                     
        d = dict(zip(keys, values))
        cfT = fixed_cost().check_cFixMT(d)
        print('aki bobalhao ', cfT, 3*'\n')
        values.append(cfT)
        keys.append('custos fixos totais')
        self.lc_fixos = values
        self.dc_fixos = dict(zip(keys, values))
        print('lista de lc_fixos', self.lc_fixos, '\n')
        print('dicionario de dc_fixos ', self.dc_fixos)
        
    def soma_dc_fixos(self, l):
          cFix_totais = 0
          for ele in l:
            cFix_totais += ele
          return print('custos fixos totais =', cFix_totais)
    
    def print_dc_fixos(self, m):
        d= self.dc_fixos                      
        import pandas as pd   
        print (3*'\n')
        print(m*'_')
        print ('{:^40}'.format('Tabela de custos fixos mensais'))
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

'''
x = fixed_cost()
x.entradas()
dc_fixos=x.dc_fixos
#x.check_cFixMT()
x.print_dc_fixos(35)
#x.soma_dc_fixos(l)
#x.check_cFixMT()
#print ('Custos Fixos Totais ', x.cmt_cfix)
'''

