user = "Professor"
senha = "1234"
contador = "s"  
print("=" * 100)
print("Boas-vindas à tela de login!")
print("=" * 100)

while contador == "s":
    user_novo = input("Qual seu usuário?: ")
    senha_novo = input("Qual a sua senha?: ")

    if user_novo == user and senha_novo == senha:
        
        break  
    else:
        print("=" * 100)
        print("Usuário ou senha incorretos.")
        print("=" * 100)
        contador = input("\nTentar novamente? (s/n): (nota: Digitar algo além de 's' acarretará no fim do programa.): ").lower()
        print("Obrigado por usar nosso programa.")
        print("=" * 100)
        print("Trabalho feito por:\n \nGustavo: encerramento \nVinicius: login \nLuiz: código\n")
        print("=" * 100)
        
        
