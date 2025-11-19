#def linha():
#    print(50*'-')

#linha() 
#print("sistema de aluno")
#linha


#def titulo(msg):
   # print(50*'-')
  #  print(msg)
 #   print(50*'-')
    
#titulo("sistema de aluno")   
#texto = input("sistema de alunos")
#titulo(texto)

#import math
#def soma(a, b, c):
#    print(f"A = {a}, B = {b} e C = {c}")
#    s = a+b+c
#    print(f"A soma de A + B + C = {s}")
 

#resultado = int(input("Digite o primeiro numero para a soma: "))
#resultado1 = int(input("digite o segundo numero para a soma: "))
#resultado2 = int(input("digite o terceiro numero: "))
#print(f"a soma dos numeros é:  ")
#soma(resultado, resultado1, resultado2  )

#def contador(* num):
 #   print(num)
#contador(2,1,7)
#contador(8,0)
#contador(4,4,7,6,2)

#def contador(* num):
#    for valor in num:
#        print(f"{valor}", end="")
#contador(2,1,7)
#contador(8,0)
#contador(4,4,7,6,2)

#def contador(* num):
  #  tam = len(num)
 #   print(f"recebi os valores{num} e são ao todo {tam} numeros")
#contador(2,1,7)
#contador(8,0)
#contador(4,4,7,6,2)

#def dobra(lst): #nome disso é parametro 
#    pos=0
#    while pos < len(lst):
#        lst[pos] *=2
#        pos +=1
#valores = [7,2,5,0,4]
#dobra(valores)
#print(valores)

def somar(a=0,b=0,c=0):
    s= a+b+c
    print("a soma vale ",s)

somar(3,4,7)




