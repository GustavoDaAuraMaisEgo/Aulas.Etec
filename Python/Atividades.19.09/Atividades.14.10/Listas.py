#pessoas=[["João",10],["Pedro",15],["José",18]]
#print(pessoas[0][0])
#print(pessoas[1][1])
#print(pessoas[2])

#test=list()
#test.append('Lindolfo')
#test.append(43)
#print(test)
#galera =list()
#galera.append(test[:])
#print(galera)
#test[0] = 'Maria'
#test[1] = 22
#galera.append(test[:])
#print(galera)

#turma = [["Ana",15],["João",20],["Pedro",32],["Raul",44]]
#print(turma)
#print(turma[0])
#print(turma[1][1])

#for p in turma:
    #print(p[0])
    #print(p[1])

#for p in turma:
    #print(p[0],"tem",p[1],"anos de idade")

#turma2 = list()
#dados=list()
#for c in range(0,6):
    #dados.append(str(input("Nome: ").upper().strip()))
    #dados.append(int(input("Idade: ").upper().strip()))
    #turma2.append(dados[:])
    #dados.clear()

turma2 = list()
dados=list()
totmaior = totmenor = 0

for c in range(0,6):
    dados.append(str(input("Nome: ").upper().strip()))
    dados.append(int(input("Idade: ").upper().strip()))
    turma2.append(dados[:])
    dados.clear()

for p in turma2:
    if p[1] >= 18:
        print(p[0],"é maior de idade",p[1],"anos de idade")
        totmaior += 1
    else:
        print(p[0],"é menor de idade",p[1],"anos de idade")
        totmenor += 1

print("Temos",totmaior,"maiores de idade e",totmenor,"menores de idade")

    
