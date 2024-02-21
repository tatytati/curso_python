# Programa para calcular IMC
# Desenvolvido por Celso

print("****************************")
print("*   CALCULADORA DE IMC     *")
print("****************************")
print()

# criaçaõ das variaveis
nome = ""
peso = 0
altura = 0.0
imc = 0.0
# entrada dos dados
nome = input("digite o seu nome: ")
peso = int(input("digite o seu peso: "))
altura = float(input("digite a sua altura: "))

# Processar os valores para obter o IMC
imc = peso / altura ** 2

situacao =""
      
if imc < 18.5:
    situacao = " abaixo do peso"
elif imc >= 18.5 and imc < 25.0:
    situacao = "Peso normal"
elif imc >= 25 and imc < 30:
    situacao = "sobre peso"
elif imc >= 30 and imc < 35:
    situacao = "obesidade grau um"
elif imc >= 35 and imc < 40:
     situacao = "obesidade grau dois"
else:
    situacao = "obesidade grau tres ou morbida"
print("**************")


#Saida do processamento
print()
print("********************")
print("*    resultado      *")
print("*********************")
print("*                   *")
print("Nome: " + nome)
print("Peso: " + str(peso)+ "kg")
print("Altura: " + str(altura)+ "m")
print("imc: " + str(imc))
print("situação: " + situacao) 
    
