print("**************")
print("*   MÉDIA FINAL    *")
print("**************")

# PROGRAMA PARA CALCULAR A MÉDIA FINAL

nome_do_aluno = ""
nota_bimestre1 = 0.0
nota_bimestre2 = 0.0
nota_bimestre3 = 0.0
nota_bimestre4 = 0.0
media_final = 0.0
#ENTRADA DOS DADOS

nome_do_aluno = input("Qual o nome do aluno? : ")
nota_bimestre1 = float(input("Nota 1: "))
nota_bimestre2 = float(input("Nota 2: "))
nota_bimestre3 = float(input("Nota 3: "))
nota_bimestre4 = float(input("Nota 4: "))

#CALCULAR A NOTA FINAL
media_final = (nota_bimestre1 + nota_bimestre2 + nota_bimestre3 + nota_bimestre4)/4

# EXIBIR O RESULTADO
print()
print("*   RESULTADO   *")
print("----------------")
print(nome_do_aluno + ", a sua nota final é " + str(media_final))

# situação

if media_final >= 7.0:
    situação = "aprovado"
elif media_final < 5:
    situação = "reprovado "   
else:
    situação = " em recuperação"

# exibir
print("**************")
print(f"{nome_do_aluno}, você esta {situação}, com média {media_final}. ")


