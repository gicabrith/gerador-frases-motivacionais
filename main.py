
import random
from frases import lista_de_frases

def mostrar_menu():
    print("\n=== GERADOR DE FRASES MOTIVACIONAIS ===")
    print("1 - Ver uma frase motivacional")
    print("2 - Sair")

while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        frase = random.choice(lista_de_frases)
        print("\n✨ Sua frase motivacional:")
        print(frase)

    elif opcao == "2":
        print("Até mais! Continue acreditando em você! 💪")
        break

    else:
        print("Opção inválida. Tente novamente.")