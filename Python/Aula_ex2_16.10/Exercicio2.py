user = "Professor"
senha = "1234"
contador = ""
while contador == "s":
    print("Boas-vindas à tela de login!")

    user_novo = str(input("Qual seu usuário?: "))
    senha_novo = str(input("Qual a sua senha?: "))

    if user_novo == user and senha == senha_novo:
        print("deu certo")
    else:
        contador = str(input("Tentar novamente? s/n"))
        print("caralho")
