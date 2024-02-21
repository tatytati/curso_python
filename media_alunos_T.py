#calculando a média final dos alunos

print("***************************")
print("* MEDIA FINAL DE ALUNOS *")
print("***************************")

#criação de variaveis
nome_do_aluno=""
bimestre_nota_1=0.0
bimestre_nota_2=0.0
bimestre_nota_3=0.0
bimestre_nota_4=0.0






#entrada de dados
nome_do_aluno= input("qual o nome do aluno? ")
bimestre_nota_1= float(input("nota 1: "))
bimestre_nota_2= float(input("nota 2: "))
bimestre_nota_3= float(input("nota 3: "))
bimestre_nota_4= float(input("nota 4: "))

media_final = (bimestre_nota_1 +bimestre_nota_2 +bimestre_nota_3 +bimestre_nota_4) / 4
print("----------------------")
print(nome_do_aluno + ", a sua nota final é "+ str(media_final))
print("----------------------")    








             

