# -*- coding: utf-8 -*-
"""
Created on Mon May  9 16:49:32 2022

@author: Windows 11
"""

class milk_data():
        
    def __init__ (self, lc_milk=[], dc_milk={}):
        
        self.lc_milk = lc_milk
        self.dc_milk = dc_milk
        
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

    def list_to_dict(self, l):
        global d
        a = iter(l)
        d = dict(zip(a, a))
        return d
    
    def check_cmilk(self):
        
        self.data_cmilk=0
        for i in self.dc_milk.keys():
            self.cmt_cmilk += self.dc_milk[i][3]
            print(self.cmt_cmilk)
        return self.cmt_cmilk
    
    def entradas(self):
        
        milk_preco = milk_data().check_float('preço do litro de leite')
        self.dc_milk['R% / litro']= [milk_preco]
        milk_ltsdia = milk_data().check_float('produção litros leite/dia')
        self.dc_milk['lts de leite/dia']= [milk_ltsdia]
        milk_qvl = milk_data().check_float('quantidade de vacas em lactação')
        self.dc_milk['total de vacas lacatacao']= [milk_qvl]
        milk_mllv = milk_ltsdia/milk_qvl
        self.dc_milk['media de lts leite/vaca']= [milk_mllv]
        milk_rday = milk_preco*milk_ltsdia
        self.dc_milk['receita em R$/dia']= [milk_rday]
        milk_pmonth = milk_ltsdia*30
        self.dc_milk['producao lts leite/mes']= [milk_pmonth]
        milk_rmonth = milk_rday*30
        self.dc_milk['receita em R$/mes']= [milk_pmonth]
        #l=self.lc_milk = [[milk_preco], [milk_ltsdia], [milk_qvl], [milk_mllv], [milk_rday], [milk_pmonth], [milk_rmonth]]
        #self.dc_milk['dados do leite'] = self.lc_milk
        print(self.dc_milk)
        self.lc_milk=list(self.dc_milk.items())
        print('\n','lc_milk', self.lc_milk)
        
        self.lc_milk=list(self.dc_milk.keys())
        
    def print_dc_milk(self, m):
        texto = "Dados da produçao de leite"                      
        import pandas as pd   
        d = self.dc_milk
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
    
    #def print_grafico():
    #pass
    
    """
    def print_test(self, m):
        
        
        import pandas as pd   
        print (36*'\n')
        print(m*'_')
        print ('{:^40}'.format('Tabela de custos fixos mensais'))
        print(m*'=')
        
        l1 = ['preço leite', 'produção leite', 'numero vacas', 'lts/vaca', 'produção/dia', 'receita/dia', 'receita/mes']
        
        #df = pd.DataFrame(d, columns = ['Name','Age','Percent']) 
        df = pd.DataFrame(self.lc_milk, columns = l1)
        #print(self.lc_milk)
        print(df)
        
        
        d = [ ["Mark", 12, 95],
             ["Jay", 11, 88],
             ["Jack", 14, 90]]

        df = pd.DataFrame(d, columns=["Name", "Age", "Percent"])
        blankIndex=[''] * len(df)  #Tira a aprimeira coluna
        df.index=blankIndex
        #print(df)
        
        df_tr = df.transpose() #Inverte Linha x Coluna no Dataframe
        #print(df.to_markdown(index=False)) 
        print(df_tr)
        df_tr.plot.line
        print(df)
        df.plot.line()
    """   
'''    
x = milk_data()   
x.entradas()
x.print_dc_milk(33)
#x.print_test(65)

#print(x.lc_milk)
#print(x.dc_milk)
'''        