# -*- coding: utf-8 -*-
"""
Created on Fri May  6 11:49:11 2022

@author: Windows 11
"""
'''
==>Racao Total Lote1
==>Racao Total Lote 2 
==>Racao TotalLote 3
==>Racao Total Lote 4 
==>Racao Total Lote 5 
==>Bezerros Grandes
==>Bezerras Medias
==>Bezerros desmamados
==>Bezerros amarrados
Sal Proteinado
Sal Comum
Leite em Po
Lactotropin
Ocitocina
Frete
'''
class var_costs():
        
    def __init__ (self, lc_var=[], dc_var={}):
        
        self.lc_var = lc_var
        self.dc_var = dc_var
        
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
    
    def check_cVarMT(self):
        
        self.cmt_cvar=0
        for key in self.dc_var.keys():
            #if key!='tipo produto':
            print(self.dc_var[key][3])
            self.cmt_cvar += self.dc_var[key][3]
                
        return print(self.cmt_cvar)
    
    def soma_dc_var(self, l):
          cVar_totais = 0
          for ele in l:
            cVar_totais += ele
          return print('custos variaveis totais =', cVar_totais)
        
    def entradas_var(self, m):
        
        print(m*'=')
        print('{:^45}'.format(' Ração dos Lote 1'))
        print(m*'_')
        '''
        l = ['consumo/cab', 'R$/Un', 'animais', 'R$/produto']
        self.lc_var = ['consumo/cab', 'R$/Un', 'animais', 'R$/produto']
        print(self.lc_var)
        self.dc_var['tipo produto']=self.lc_var
        print(self.dc_var)
        '''
        #print(45*'=','\n')
        rl1_kgd = var_costs().check_float('consumo em kg/dia/animal ração do lote 1')
        rl1_ckr = var_costs().check_float('custo por Kg ração do lote 1')
        rl1_qa = var_costs().check_float('qtde animais ração do lote 1')
        rl1_cm = rl1_kgd*rl1_ckr*rl1_qa*30 #custo mensal ração do lote 1
        self.lc_var = [rl1_kgd, rl1_ckr, rl1_qa, rl1_cm]
        print(self.lc_var)
        self.dc_var['ração lote 1'] = self.lc_var
        print(self.dc_var)
        '----------------------lote 2----------------------------------'
        print(m*'=')
        print('{:^45}'.format(' Ração dos Lote 2'))
        print(m*'=')
        rl2_kgd = var_costs().check_float('consumo/dia/animal ração do lote 2')
        rl2_ckr = var_costs().check_float('custo por kg  ração do lote 2')
        rl2_qa = var_costs().check_float('qtde animais ração do lote 2')
        rl2_cm = rl2_kgd*rl2_ckr*rl2_qa*30 #custo mensal ração do lote 2
        self.lc_var = [rl2_kgd, rl2_ckr, rl2_qa, rl2_cm]
        print(self.lc_var)
        self.dc_var['ração lote 2'] = self.lc_var
        print(self.dc_var)
        '----------------------lote 3----------------------------------'
        print(m*'=')
        print('{:^45}'.format(' Ração dos Lote 3'))
        print(m*'=')
        rl3_kgd = var_costs().check_float('consumo/dia/animal ração do lote 3')
        rl3_ckr = var_costs().check_float('custo por kg  ração do lote 3')
        rl3_qa = var_costs().check_float('qtde animais ração do lote 3')
        rl3_cm = rl3_kgd*rl3_ckr*rl3_qa*30 #custo mensal ração do lote 3
        self.lc_var = [rl3_kgd, rl3_ckr, rl3_qa, rl3_cm]
        print(self.lc_var)
        self.dc_var['ração lote 3'] = self.lc_var
        print(self.dc_var)
        
        """
        
        '----------------------lote 4----------------------------------'
        print(m*'=')
        print('{:^45}'.format(' Ração dos Lote 4'))
        print(m*'=')
        rl4_kgd = var_costs().check_float('consumo/dia/animal ração do lote 4')
        rl4_ckr = var_costs().check_float('custo por kg  ração do lote 4')
        rl4_qa = var_costs().check_float('qtde animais ração do lote 4')
        rl4_cm = rl4_kgd*rl4_ckr*rl4_qa*30 #custo mensal ração do lote 4
        self.lc_var = [rl4_kgd, rl4_ckr, rl4_qa, rl4_cm]
        print(self.lc_var)
        self.dc_var['ração lote 4'] = self.lc_var
        print(self.dc_var)
        '----------------------lote 5----------------------------------'
        print(m*'=')
        print('{:^45}'.format(' Ração dos lote 5'))
        print(m*'=')
        rl5_kgd = var_costs().check_float('consumo/dia/animal ração do lote 5')
        rl5_ckr = var_costs().check_float('custo por kg  ração do lote 5')
        rl5_qa = var_costs().check_float('qtde animais ração do lote 5')
        rl5_cm = rl5_kgd*rl5_ckr*rl5_qa*30 #custo mensal ração do lote 5
        self.lc_var = [rl5_kgd, rl5_ckr, rl5_qa, rl5_cm]
        print(self.lc_var)
        self.dc_var['ração lote 5'] = self.lc_var
        print(self.dc_var)
        '----------------------bezerros grandes-----------------------------------'        
        print(m*'=')
        print('{:^45}'.format(' Ração dos bezerros grandes'))
        print(m*'=')
        rbg_kgd = var_costs().check_float('consumo/dia/animal ração do bezerros grandes')
        rbg_ckr = var_costs().check_float('custo por kg  ração do bezerros grandes')
        rbg_qa = var_costs().check_float('qtde animais ração do bezerros grandes')
        rbg_cm = rbg_kgd*rbg_ckr*rbg_qa*30 #custo mensal ração do bezerros grandes
        self.lc_var = [rbg_kgd, rbg_ckr, rbg_qa, rbg_cm]
        print(self.lc_var)
        self.dc_var['ração bezerros grandes'] = self.lc_var
        print(self.dc_var)
        '----------------------bezerras medias-----------------------------------'        
        print(m*'=')
        print('{:^45}'.format(' Ração das bezerras medias'))
        print(m*'=')
        rbm_kgd = var_costs().check_float('consumo/dia/animal ração do bezerras medias')
        rbm_ckr = var_costs().check_float('custo por kg  ração do bezerras medias')
        rbm_qa = var_costs().check_float('qtde animais ração do bezerras medias')
        rbm_cm = rbm_kgd*rbm_ckr*rbm_qa*30 #custo mensal ração do bezerras medias
        self.lc_var = [rbm_kgd, rbm_ckr, rbm_qa, rbm_cm]
        print(self.lc_var)
        self.dc_var['ração bezerras medias'] = self.lc_var
        print(self.dc_var)
        '----------------------bezerros desmamados-----------------------------------'        
        print(m*'=')
        print('{:^45}'.format(' Ração dos bezerros desmamados'))
        print(m*'=')
        rbd_kgd = var_costs().check_float('consumo/dia/animal ração dos bezerros desmamados')
        rbd_ckr = var_costs().check_float('custo por kg  ração dos bezerros desmamados')
        rbd_qa = var_costs().check_float('qtde animais ração dos bezerros desmamados')
        rbd_cm = rbd_kgd*rbd_ckr*rbd_qa*30 #custo mensal ração dos bezerros desmamados
        self.lc_var = [rbd_kgd, rbd_ckr, rbd_qa, rbd_cm]
        print(self.lc_var)
        self.dc_var['ração bezerros desmamados'] = self.lc_var
        print(self.dc_var)
        '----------------------bezerros mamando-----------------------------------'        
        print(m*'=')
        print('{:^45}'.format(' ração dos bezerros mamando'))
        print(m*'=')
        rbma_kgd = var_costs().check_float('consumo/dia/animal ração dos bezerros mamando')
        rbma_ckr = var_costs().check_float('custo por kg  ração dos bezerros mamando')
        rbma_qa = var_costs().check_float('qtde animais ração dos bezerros mamando')
        rbma_cm = rbma_kgd*rbma_ckr*rbma_qa*30 #custo mensal ração dos bezerros mamando
        self.lc_var = [rbma_kgd, rbma_ckr, rbma_qa, rbma_cm]
        print(self.lc_var)
        self.dc_var['ração bezerros mamando'] = self.lc_var
        print(self.dc_var)
        '----------------------sal proteinado-----------------------------------'        
        print(m*'=')
        print('{:^45}'.format(' sal proteinado'))
        print(m*'=')
        sp_kgd = var_costs().check_float('consumo/dia/animal sal proteinado')
        sp_ckr = var_costs().check_float('custo por kg  sal proteinado')
        sp_qa = var_costs().check_float('qtde animais sal proteinado')
        sp_cm = sp_kgd*sp_ckr*sp_qa*30 #custo mensal sal proteinado
        self.lc_var = [sp_kgd, sp_ckr, sp_qa, sp_cm]
        print(self.lc_var)
        self.dc_var['sal proteinado'] = self.lc_var
        print(self.dc_var)
        '----------------------sal mineral-----------------------------------'        
        print(m*'=')
        print('{:^45}'.format(' sal mineral'))
        print(m*'=')
        sm_kgd = var_costs().check_float('consumo/dia/animal sal mineral')
        sm_ckr = var_costs().check_float('custo por kg  sal mineral')
        sm_qa = var_costs().check_float('qtde animais sal mineral')
        sm_cm = sm_kgd*sm_ckr*sm_qa*30 #custo mensal sal mineral
        self.lc_var = [sm_kgd, sm_ckr, sm_qa, sm_cm]
        print(self.lc_var)
        self.dc_var['sal mineral'] = self.lc_var
        print(self.dc_var)
        '----------------------leite em po-----------------------------------'        
        print(m*'=')
        print('{:^45}'.format(' leite em po'))
        print(m*'=')
        lp_ltd = var_costs().check_float('consumo em lts/dia/animal leite em po')
        lp_ckr = var_costs().check_float('custo por kg  leite em po')
        lp_qa = var_costs().check_float('qtde animais leite em po')
        lp_cm = sp_kgd*sp_ckr*sp_qa*30 #custo mensal leite em po
        self.lc_var = [lp_ltd, lp_ckr, lp_qa, lp_cm]
        print(self.lc_var)
        self.dc_var['leite em po'] = self.lc_var
        print(self.dc_var)
        '----------------------lactotropin-----------------------------------'        
        print(m*'=')
        print('{:^45}'.format(' lactotropin'))
        print(m*'=')
        lac_cul = var_costs().check_float('custo unitario de 1 lactotropin')
        lac_ida = var_costs().check_float('intervalo de dias para aplicar lactotropin')
        lac_qa = var_costs().check_float('qtde animais lactotropin')
        lac_cm = (30/lac_ida)*lac_cul*lac_qa #custo mensal lactotropin
        self.lc_var = [lac_cul, lac_ida, lac_qa, lac_cm]
        print(self.lc_var)
        self.dc_var['lactotropin'] = self.lc_var
        print(self.dc_var)
        '----------------------ocitocina-----------------------------------'        
        print(m*'=')
        print('{:^45}'.format('ocitocina'))
        print(m*'=')
        oci_mld = var_costs().check_float('consumo em ml/dia/animal ocitocina')
        oci_cpf = var_costs().check_float('custo por frasco ocitocina')
        oci_mpf = var_costs().check_float('quantidade ml por frasco ocitocina')
        oci_qa = var_costs().check_float('qtde animais ocitocina')
        oci_cm = (oci_cpf/oci_mpf)*oci_mld*oci_qa*30 #custo mensal ocitocina
        self.lc_var = [oci_mld, (oci_cpf/oci_mpf), oci_qa, oci_cm]
        print(self.lc_var)
        self.dc_var['ocitocina'] = self.lc_var
        print(self.dc_var)
        '----------------------frete-----------------------------------'        
        print(m*'=')
        print('{:^45}'.format('frete'))
        print(m*'=')
        frt_cm = var_costs().check_float('custo mensal fretes')
        self.lc_var = [0, 0, 0, frt_cm]
        print(self.lc_var)
        self.dc_var['frete'] = self.lc_var
        
        """
        '---------------custos variaveis total-----------------------------------'        
        
        self.lc_var = [0,0,0,rl1_cm+rl2_cm+rl3_cm]
        '''
        +rl4_cm+rl5_cm+rbg_cm+rbm_cm
                                    +rbd_cm+rbma_cm+sp_cm+sm_cm+lp_cm+lac_cm
                                    +oci_cm+frt_cm]
        '''
        self.dc_var['Custos Totais Variaveis'] = self.lc_var                       
                                            
        
    
    def print_dc_var(self, m):
                              
        import pandas as pd 
        d = self.dc_var
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
        lval = list(self.dc_var.values())
        lval.insert(0,l)
        lval.insert(1,l1)
        lval.insert(2,l2)
        lkey = list(self.dc_var.keys())
        lkey.insert(0,'tipo de produto')
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
x = var_costs([],{})
x.entradas_var(45)
x.check_cVarMT()
x.print_dc_var(45)
print('Custos Totais Variaveis',28*' ', x.cmt_cvar)
'''