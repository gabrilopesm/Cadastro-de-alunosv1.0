from iniciar_sistema import *

comando = '0'
while comando != '3':

    print("┌────────────────────────────────────────────────────────┐")
    print("│                      POPULUS DB                        │")
    print("│           Open-Source Database Management              │")
    print("├────────────────────────────────────────────────────────┤")
    print("│  [1] Iniciar Sistema                                   │")
    print("│  [2] Créditos & Licença                                │")
    print("│  [3] Sair                                              │")
    print("├────────────────────────────────────────────────────────┤")
    print("│  Digite o comando ou o número da opção desejada.       │")
    print("└────────────────────────────────────────────────────────┘")
    print(" Copyleft (c) 2026 Populus Tech - Alguns direitos reservados.")
    print(" Distribuído sob a Licença Creative Commons (CC BY-SA 4.0)")
    print()

    comando = input("populus-db > ")

    if comando == "1" or comando == "Iniciar Sistema":
        pass

    elif comando == "2" or comando == "Créditos":
        pass

    elif comando == '3' or comando == 'Sair':
        pass

print("Fim do programa.")