import os

print('ℙ𝕚𝕫𝕫𝕒 ℙ𝕝𝕒𝕟𝕖𝕥')
print("""
[1] Cadastrar restaurante
[2] Listar restaurante
[3] Ativar restaurante
[4] Sair""")

#ENTRADA DE DADOS
opção = int(input('Escolha uma opção: '))

#ENCERRA O PROGRAMA
def finalizar_app():
    os.system('cls')
    print("Encerrando App...\n")

#CONDIÇÃO
if opção == 1:
    print('Cadastrar restaurante')
elif opção == 2:
    print('Listar restaurantes')
elif opção == 3: 
    print('Ativar restaurante')
else:
    finalizar_app()