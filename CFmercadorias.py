class entradas():
    def __init__(self, 
                 nucleoCorte = 130, nucleoCorte_kg = 30,
                 volumoso = 300, volumoso_kg = 1000,
                 racao = 120, racao_kg = 40,
                 fareloSoja = 180, fareloSoja_kg = 50, 
                 bicarb = 85, bicarb_kg = 25, 
                 salMineral = 65, salMineral_kg = 30,
                 produtos = { }):
                 
        
        self.produtos = {}
        self.nucleoCorte = nucleoCorte
        self.nucleoCorte_kg = nucleoCorte_kg
        
        self.volumoso= volumoso
        self.volumoso_kg = volumoso_kg
        
        self.racao = racao
        self.racao_kg = racao_kg
        
        self.fareloSoja = fareloSoja
        self.fareloSoja_kg = fareloSoja_kg
        
        self.bicarb = bicarb
        self.bicarb_kg = bicarb_kg
        
        self.salMineral = salMineral
        self.salMineral_kg = salMineral_kg
    
    
    def checkErrFloat(self, texto):
        
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
    
   
    def valores(self, m):
    
        print (m*'_')   #Entrada dados nucleo
        self.nucleoCorte = entradas().checkErrFloat('preço saca de nucleoCorte')
        self.nucleoCorte_kg = entradas().checkErrFloat('peso saca de nucleoCorte')
        self.produtos['nucleoCorte'] = [self.nucleoCorte, self.nucleoCorte_kg, round((self.nucleoCorte/self.nucleoCorte_kg),2)]

        print (m*'_')   #Entrada dados nucleo
        self.volumoso = entradas().checkErrFloat('preço do volumoso por tonelada')
        #self.volumoso_kg = entradas().checkErrFloat('peso saca de volumoso')
        self.produtos['volumoso'] = [self.volumoso, 1.000, round((self.volumoso/1000),2)]

        print (m*'_')   #Entrada dados nucleo
        self.racao = entradas().checkErrFloat('preço saca de racao')
        self.racao_kg = entradas().checkErrFloat('peso saca de racao')
        self.produtos['racao'] = [self.racao, self.racao_kg, round((self.racao/self.racao_kg),2)]

        print (m*'_')   #Entrada dados nucleo
        self.fareloSoja = entradas().checkErrFloat('preço saca de fareloSoja')
        self.fareloSoja_kg = entradas().checkErrFloat('peso saca de fareloSoja')
        self.produtos['fareloSoja'] = [self.fareloSoja, self.fareloSoja_kg, round((self.fareloSoja/self.fareloSoja_kg),2)]

        print (m*'_')   #Entrada dados nucleo
        self.bicarb = entradas().checkErrFloat('preço saca de bicarb')
        self.bicarb_kg = entradas().checkErrFloat('peso saca de bicarb')
        self.produtos['bicarb'] = [self.bicarb, self.bicarb_kg, round((self.bicarb/self.bicarb_kg),2)]

        print (m*'_')   #Entrada dados nucleo
        self.salMineral = entradas().checkErrFloat('preço saca de salMineral')
        self.salMineral_kg = entradas().checkErrFloat('peso saca de salMineral')
        self.produtos['salMineral'] = [self.salMineral, self.salMineral_kg, round((self.salMineral/self.salMineral_kg),2)]

    def print_produtos(self, m):
                              
        import pandas as pd 
        d = self.produtos
        print (26*'\n')
        print(m*'_')
        print ('{:^75}'.format('Tabela de Produtos'))
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


x = entradas()
x.valores(45)
#x.nucleoCorte

x.print_produtos(45)
produtos=x.produtos
print(produtos)

'@@@@@@@@@@@@@@@@@__Save arquivo___@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
import json
#arquivo = {'milho': [2.0, 2.0, 1.0], 'nucleo': [2.0, 2.0, 1.0], 'silo': [2.0, 1000, 0.0], 'ração': [2.0, 2.0, 1.0], 'bicarbonato': [2.0, 2.0, 1.0], 'sal_mineral': [2.0, 2.0, 1.0], 'arroba_boi': [2.0, 2.0, 0]}
produtos = json.dumps(produtos,  indent=True)
with open ("produtos.json", 'w+') as file:
    file.write(produtos)
'@@@@@@@@@@@@@@@@@__Fim Save arquivo___@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'

print('@@@@@@@@@@@@@@@@@@@@@@@@@@@ Read Arquivo @@@@@@@@@@@@@@@@@@@@@@@@@@@')
import json
with open('produtos.json', 'r+') as file:
    produtos = file.read()
    produtos = json.loads(produtos)
    print('______________________________________________')
    print('produtos: ', produtos, '\n')
    print('______________________________________________')

'@@@@@@@@@@@@_____Fim Leitura e print arquivo lido______@@@@@@@@@@@@@@@@@@@@'

