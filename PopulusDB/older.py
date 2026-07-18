opcao = 0
alunos_matriculados = []


def nova_matricula(lista):
    nome_aluno = input("Nome completo: ")
    idade_aluno = int(input("Idade: "))
    altura_aluno = float(input("Altura: "))

    # Armazenar os dados em um dicionário
    novo_aluno = {
        "Nome": nome_aluno,
        "Idade": idade_aluno,
        "Altura": altura_aluno
    }

    # Inserir o dicionário dentro da lista
    lista.append(novo_aluno)


def consulta_alunos(lista):
    if lista:
        print("===== Lista de alunos cadastrados: =====\n")
        # No caso, é obrigatório fazer um for para mostrar toda a lista na tela, porque o for percorre todos os elementos da lista e vai armazenando em uma variável. Só assim para conseguir buscar os elementos dentro de cada dicionário da lista

        for alunos in lista:
            print(f"Nome: {alunos['Nome']} \nIdade: {alunos['Idade']} anos \nAltura: {alunos['Altura']}")

    else:
        print('\nNenhum aluno cadastrado :(')


while opcao != 3:

    print("""
        Digite o número referente ao comando desejado

            1 - Nova Matrícula
            2 - Lista de alunos matrículados
            3 - Encerrar atendimento""")
    opcao = int(input("\nDigite a opção desejada: "))

    if opcao == 1:
        nova_matricula(alunos_matriculados)

    elif opcao == 2:
        consulta_alunos(alunos_matriculados)

    elif opcao == 3:
        print("Obrigado por utilizar o nosso softaware.")

    else:
        print("Opção inválida. Tente novamente!")

print("Fim do programa")

""" E se eu quisesse consultar o nome de um aluno específico, o que eu teria que fazer?
    elif opcao == 4:
           for alunos in alunos_matriculados:
            if 'Gabriel' in alunos["Nome"]:
                print("Aluno cadastrado")
            else:
                print('Nenhum aluno encontrado')"""