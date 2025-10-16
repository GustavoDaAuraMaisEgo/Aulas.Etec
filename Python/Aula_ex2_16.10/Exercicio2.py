user = "Professor"
senha = "1234"
contador = "s"  

print("Boas-vindas à tela de login!")

while contador == "s":
    user_novo = input("Qual seu usuário?: ")
    senha_novo = input("Qual a sua senha?: ")

    if user_novo == user and senha_novo == senha:
        
        break  
    else:
        print("Usuário ou senha incorretos.")
        contador = input("\nTentar novamente? (s/n): ").lower()
        print("Obrigado por usar nosso programa.")
