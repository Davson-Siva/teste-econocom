#from main import *
from func_produtos import *

def menu_produtos():
    acao = input("digite algo: ")
    if acao == "5":
        edit = input("Qual será a ação tomada? \n1 = ADICIONAR UM PRODUTO \n2 = REMOVER UM PRODUTO \n3 = EDITAR UM PRODUTO: ")

        if edit == "1":
            continuar = "y"
            while continuar == "y":
                print("ADICIONANDO PRODUTO.")
                nome_produto = input("Qual o nome do produto? ")
                valor_produto = input("Digite o valor do produto: ")
                if(adiciona_produto(path_final_produtos, nome_produto, valor_produto)):
                    print("PRODUTO ADICIONADO")
                adicionar = input("Deseja adicionar mais produtos? Y/N ")
                while adicionar.lower() == "y":
                    nome_produto = input("Qual o nome do produto? ")
                    valor_produto = input("Digite o valor do produto: ")
                    if(adiciona_produto(path_final_produtos, nome_produto, valor_produto)):
                        print("PRODUTO ADICIONADO")
                        
                    continuar = input("Deseja adicionar mais produtos? Y/N: ")
                    while continuar.lower() != "y" and continuar.lower() != "n":
                        print("OPÇÃO INVÁLIDA.")
                        continuar = input("Deseja adicionar mais produtos? Y/N: ")
                    if continuar.lower == "y":
                        continue
                    else:
                        return True
            
        elif edit == "2":
            continuar = "y"
            while continuar == "y":
                print("REMOVENDO PRODUTO")
                pega_lista_produtos(path_final_produtos)
                produto = input("Digite o código do produto que será excluído: ")
                valido = verifica_codigo_pedido(produto)
                while valido == False:
                    produto = input("Código inválido. Insira somente o código do produto: ")
                    valido = verifica_codigo_pedido(produto)
                if(remove_produto(path_final_produtos, produto)):
                    print("PRODUTO REMOVIDO.")
                    continuar = input("Deseja remover mais intens? Y/N ")
                    while continuar.lower() != "y" and continuar.lower() != "n":
                        print("OPÃO INVALIDA")
                        continuar = input("Deseja remover mais intens? Y/N ")

                    if ccontinuar == "y":
                        continue
                    else:
                        return True
        elif edit == "3":
            continuar = "y"
            while continuar == "y":
                print("EDITANDO PRODUTO")
                pega_lista_produtos(path_final_produtos)
                produto = input("Insira somente o código do produto que deseja editar: ")

                valido = verifica_codigo_pedido(produto)
                print("Validação de código. " + str(valido))

                while valido == False:
                    produto = input("Código inválido. Insira somente o código do produto que deseja editar: ")
                    valido = verifica_codigo_pedido(produto)
                editar = input("1 = ALTERAR NOME DO PRODUTO: \n2 = ALTERAR PREÇO DO PRODUTO: ")
                if editar == "1":
                    novo_nome = input("Qual o novo nome para o produto? ")
                    edita_nome_produto(produto, novo_nome, path_final_produtos)
                    continuar = input("Deseja alterar mais intens? Y/N")
                    while continuar.lower() != "y" and continuar.lower() != "n":
                        print("OPÇÃO INVÁLIDA.")
                        continuar = input("Deseja alterar mais itens? Y/N ")

                    if continuar == "y":
                        continue
                    else:
                        return True
                    
                elif editar == "2":
                    print("Alterar preço")
