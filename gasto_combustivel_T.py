
print("---------------------------")
print("* consumo de combustivel *")
print("---------------------------")
print()

#criação de variaveis

modelo_do_carro= ""  
autonomia= 0
distancia_da_viagem= 0
valor_do_combustivel= 0.0
quantidade_de_combustivel_usado= 0.0
valor_gasto= 0.0

# entrada de dados
modelo=input("qual o modelo do carro? ")
autonomia=int(input("digite autonomia do carro? "))
distancia_da_viagem=int(input("digite a distancia da viagem: "))
valor_do_combustivel=float(input("digite o valor: "))

#processar dados

quantidade_de_combustivel_usado = distancia_da_viagem / autonomia
valor_gasto = quantidade_de_combustivel_usado * valor_do_combustivel

#saida
print("---------------------------")
print("* resultado *")
print("---------------------------")
print("modelo do veiculo:" + modelo)
print("autonomia do veiculo: "+ str(autonomia) + "km")
print("distancia percorida: "+ str(distancia_da_viagem))
print("valor do combustivel: "+ str(valor_do_combustivel))
print()
print(f"quantidade de combustivel usado: {quantidade_de_combustivel_usado:.2f} L")
print("total gasto com viagem: {valor_gasto:.2f}")
print("---------------------------")

5==5







