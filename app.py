import os
def program_name():
    print('ℙ𝕚𝕫𝕫𝕒 ℙ𝕝𝕒𝕟𝕖𝕥')

def mostrar_opcoes():
    print("""          
    [1] Cadastrar restaurante
    [2] Listar restaurante
    [3] Ativar restaurante
    [4] Sair""")
#ENCERRA O PROGRAMA
def finalizar_app():
    os.system('cls')
    print("Encerrando App...\n")

def escolher_opcao():
    #ENTRADA DE DADOS
    opção = int(input('Escolha uma opção: '))

    #CONDIÇÃO
    if opção == 1:
        print('Cadastrar restaurante')
    elif opção == 2:
        print('Listar restaurantes')
    elif opção == 3: 
        print('Ativar restaurante')
    else:
        finalizar_app()

def main():
    program_name()
    mostrar_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()