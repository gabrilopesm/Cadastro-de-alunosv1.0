from older import alunos_matriculados

comando = ''
alunos_matriculados= []

def novo_cadastro(lista):
    nome_aluno = input("Nome > ")
    idade_aluno = input("Idade > ")
    telefone_aluno = input("Telefone > ")

    novo_aluno = {
        "nome": nome_aluno,
        "idade": idade_aluno,
        "telefone": telefone_aluno
    }

    lista.append(novo_aluno)


while comando != '4':

    def iniciar_sistema():
        print("┌────────────────────────────────────────────────────────┐")
        print("│  [1] Novo Cadastro                                     │")
        print("│  [2] Consultar Cadastros                               │")
        print("│  [3] Listar todos                                      │")
        print("│  [4] Retornar ao Menu anterior                         │")
        print("├────────────────────────────────────────────────────────┤")
        print("│  Digite o comando ou o número da opção desejada.       │")
        print("└────────────────────────────────────────────────────────┘")

        comando = input("\npopulus-db > ")

        if comando == "1" or comando == "Novo Cadastro":
            novo_cadastro(alunos_matriculados)
            print(alunos_matriculados)

        elif comando == "2" or comando == "Consultar Cadastros":
            pass

        elif comando == '3' or comando == 'Listar':
            pass

        else:
            pass

    def novo_cadastro():
        pass