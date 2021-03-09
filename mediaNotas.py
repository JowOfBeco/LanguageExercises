def regMedia(nomeAluno):
    media = 0.0
    qtdNotas = int(input("Digite quantidade de notas para média:\n"))
    for i in range(qtdNotas):
        print("Digite a nota:", i+1, "do aluno", nomeAluno, ":\n")
        notas = float(input())
        media = media + notas
    media = media / qtdNotas
    print('A média do aluno', nomeAluno,' é :', media)
    return media
    
#---- var declaradas
qtdAlunos = int(input("Quantos alunos deseja cadastrar?\n"))

for i in range(qtdAlunos):
    if i == 0 :
        i = i+1
    nomeAluno = input("Digite o nome do Aluno:\n")
    regMedia(nomeAluno)