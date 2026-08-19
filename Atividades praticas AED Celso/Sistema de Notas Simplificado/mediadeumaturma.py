alunos_aprovados = []
alunos_reprovados = [] 
soma_da_media_turma= 0 
print("--" * 30)
print("📊 Bem vindo ao relatório da sua turma! \n"
"📊 Neste relatório só é possível o calculo de 5 alunos por vez.")
print("--" * 30)
for aluno in range(5):
    aluno=input("Qual o nome do aluno? \n")
    soma_nota = 0
    for nota in range(3):
            while True:
                nota = float(input("Qual a nota(a) dele(a)  " ))
                if nota > 10 or nota < 0:
                    print("Nota inválida! Digite uma nota de 0 a 10.")
                    continue
                else:
                    break 
            soma_nota += nota

    media = soma_nota/3
    soma_da_media_turma += media
    print(f"A média do aluno {aluno} é igual a {media:.2f}")   
    dados_dos_alunos=f"-{aluno} (Média:{media:.2f})"
    if media>=7:
        alunos_aprovados.append(dados_dos_alunos)
        print("Aluno aprovado!")
    else:
        alunos_reprovados.append(dados_dos_alunos)
        print("Aluno reprovado!")  
print("--"* 30)
print("📊 Relatório final da turma!")
print(f"Total de alunos aprovados {alunos_aprovados}")
print(f"Total de alunos reprovados {alunos_reprovados}")

media_turma=soma_da_media_turma/5
print(f"Média da turma: {media_turma}")
print("--"* 30)