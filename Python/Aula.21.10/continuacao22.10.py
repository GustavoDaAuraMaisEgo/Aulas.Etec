#materia = dict()
curso = list()

#for c in range (0,3):
#    materia ['sigla'] = str(input("digite a sigla da materia, filho da puta: "))
#    materia ['nome'] = str(input("digite a nome da materia, filho da puta: "))
#    curso.append(materia.copy())
#print(curso)
#for m in curso:
    #for k,v in m.items():
        #print("o campo",k,"tem valor",v)   

#lista = []
#dic=dict()

#nome = input("digite: ")
#idade = int(input("digite: "))
#lista.append(nome)
#lista.append(idade)
#dic={"nome":lista[0], "idade":lista[1]}
#print(lista)
#print(dic['nome'])

dados = {
    'crossfox': {'km': 35000, 'ano': 2005},
    'DS5': {'km': 17000, 'ano': 2015},
    'fusca': {'km': 130000, 'ano': 1979},
    'jetta': {'km': 56000, 'ano:': 2011},
    'passat': {'km': 62000, 'ano': 1999},
}
for item in dados.items():
    print(item)
for item in dados.items():
    print(item[1]['ano'])