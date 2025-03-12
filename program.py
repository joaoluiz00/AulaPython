# print("Olá Mundo!")
# print("Romero 3 gols hoje!")

# variavel = 127.65
# variavel =  10
# variavel = "Joao"
# variavel = ["banana", "Uva", "abacaxi"]
# variavel = True

#exibindo o valor da variavel
# print(variavel)



nome = input("Digite seu nome: ")
idade = input("digite sua idade: ")
altura = input("Digite sua altura: ")
print("Olá, seu nome é " + nome "possui " + idade "e tem " + altura" de altura")

fah = float(input("Digite o fahrenheit: "))

cel = (fah -32) * 5/9

print("O resultado é " + str(cel ))


np1 = float(input("Digite a nota 1: "))
np2 = float(input("Digite a nota 2: "))

mf = (np1 + np2 ) /2

if mf >= 5:
  print("parabens aprovado")
elif mf >= 3 and mf  < 5:
  print("Ficou de exame pae")
else:
  print("Reprovado")