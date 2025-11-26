import random
random.random
competidores = {}
def cadastro():
    nome = input("Nome do Skatista: ")
    manobras = int(input("Quantas manobras?: "))
    
    notas = []
    
    for i in range(manobras):
        nota = float(input(f"Nota da manobra {i+1}: "))
        notas.append(nota)

    notas_validas = notas[:]
    if len(notas) >= 3:
        notas_validas.remove(max(notas_validas))
        notas_validas.remove(max(notas_validas))

    media = sum(notas_validas)/len(notas_validas)

    competidores[nome] = {
        "notas":notas,
        "validas":notas_validas,
        "media":media
}
def aleatorio():
    x = random.random * 10
    print(x)

def ranking():
    print("\n---RANKING FINAL---")
    ordem = sorted(competidores.items(),key=lambda x: x[1]['media'],reverse = True)
    for i, (nome, dados) in enumerate(ordem, 1):
        print(f"{i}º - {nome} ({dados['media']:.2f})")

while True:
    print("\n---COMPETIÇÃO DE SKATE---\n1 - CADASTRAR SKATISTA\n3 - MOSTRAR RANKING\n4 - SAIR")

    op = input("Escolha:")
    if op == "1":
        cadastro()
    elif op == "2":
        ranking()
    elif op == "3":
        aleatorio()
    elif op == "4":
        break
    else:
        print("Opção invalida")