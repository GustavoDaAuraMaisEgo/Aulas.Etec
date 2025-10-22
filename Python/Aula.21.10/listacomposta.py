#lista = {}
#lista=dict()#dicionario vazio 
lista=dict()
lista={'nome':'Pedro', 'idade': 25}
#print(lista['nome'])
#print(lista['idade'])
#print("seu nome é",lista['nome'],"e sua idade é",lista['idade'],"anos ")
lista['sexo']='M'
#print(lista['sexo'])
del lista ['idade']
#print(lista)
filme = {'titulo': 'sharknado',
          'ano': 2013,
          'diretor': 'Anthony C. Ferrante'}
#print(filme.values())#valores
#print(filme.keys())#campos
#print(filme.items())
for k, v, in filme.items():
    print(f'0 {k} é {v}')
pessoas = {'nome': 'Adrubal', 'idade': 19, 'sexo': 'F'}
pessoas['peso']=95
for k,v in pessoas.items():
    print(k," = ", v)
Brasil=[]
Estado={'uf':'São Paulo','sigla': 'SP'}
Estado2={'uf':'Rio de Janeiro','sigla': 'RJ'}

Brasil.append(Estado)
Brasil.append(Estado2)

print(Brasil)
print(Brasil[0])
print(Brasil[1])

for v in Brasil.items():
    print(Brasil[1])