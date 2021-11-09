from func_pedidos import *
from func_clientes import verifica_telefone
#from func_main import menu_main

dir_path = os.path.dirname(os.path.realpath(__file__))
path_final_produtos = dir_path + str("\produtos.txt")
path_final_pedidos = dir_path + str("\pedidos.txt")
        

def menu_pedidos():
    pega_lista_produtos(path_final_produtos)

    itens = []

    produto = input("Insira somente o código do produto: ")

    valido = verifica_codigo_pedido(produto)   
    while valido == False:
        produto = input("Código inválido. Insira somente o código do produto: ")
        valido = verifica_codigo_pedido(produto)
        

    if(type(adiciona_pedido_na_lista(produto, itens )) == list):
       print("PEDIDO ADICIONADO COM SUCESSO.")
    else:
        print("ERRO AO ADICIONAR PEDIDO")

    inserir_mais_itens = input("Deseja inserir mais itens ao pedido? Y/N. Digite 'R' para remover um pedido da lista. ")
    while inserir_mais_itens.lower() != 'n':
        while inserir_mais_itens.lower() != "y" and inserir_mais_itens.lower() != "n" and inserir_mais_itens.lower() != "r":
            print("Opção inválida. Por favor, digitar 'Y', 'N' ou 'R' para indicar se quer adicionar\remover pedidos. ")
            inserir_mais_itens = input("Deseja inserir mais itens ao pedido? Y/N. Digite 'R' para remover um pedido da lista. ")
        while inserir_mais_itens.lower() == "r":
                  pega_lista_produtos(path_final_produtos)
                  print("Pedido atual: \n" + str(itens))
                  pedido_excluir = input(str("Qual o código do produto que deseja remover? "))
                  item_removido = remove_item_pedido(itens, pedido_excluir)
                  if(item_removido == False):
                      print("Código do produto não inserido na lista do pedido...")
                      time.sleep(2)
                  print("ITEM REMOVIDO COM SUCESSO")
                  continuar_removendo = input("Deseja remover outro item? Y/N ")
                  if continuar_removendo.lower() == 'y':
                      continue

                  if continuar_removendo.lower() == 'n':
                      inserir_mais_itens = input("Deseja inserir mais itens ao pedido? Y/N.")
                      while inserir_mais_itens.lower() != "y" and inserir_mais_itens.lower() != "n":
                          print("Opção inválida. Por favor, digitar 'Y', 'N' ou 'R' para indicar se quer adicionar\remover pedidos. ")
                  while itens == [] and inserir_mais_itens.lower() != 'y' and inserir_mais_itens.lower() != 'n':
                      inserir_mais_itens = input("Lista de pedidos vazia. Deseja adicionar pedidos? Y/N ")
                      while inserir_mais_itens.lower() != 'y' and inserir_mais_itens.lower() != 'n':
                          print("Opção inválida. Favor digitar somente 'Y' ou 'N'")
                          inserir_mais_itens = input("Deseja adicionar pedidos? Y/N ")

                      
                  
        while inserir_mais_itens.lower() == "y":
            pega_lista_produtos(path_final_produtos)
            produto = input("Insira somente o código do produto: ")
            valido = verifica_codigo_pedido(produto)
            while valido == False:
                produto = input("Código inválido. Insira somente o código do produto: ")
                valido = verifica_codigo_pedido(produto)
       
            if(type(adiciona_pedido_na_lista(produto, itens)) == list):
               print("PEDIDO ADICIONADO COM SUCESSO.")
            else:
                print("ERRO AO ADICIONAR PEDIDO")
            inserir_mais_itens  = input("Deseja inserir mais itens ao pedido? Y/N. Digite 'R' para remover um pedido da lista. ")

            if inserir_mais_itens == 'n':
                print("saindo")
                break
            else:
                continue




    quantidade_pedido = pega_quantidade_pedido_atual(itens)
    print("Quantidade de lanches do pedido: " + str(quantidade_pedido))
    info_completa_pedido = informacao_completa_pedido(itens, quantidade_pedido)
    print("info completa", info_completa_pedido)
    

    resultado = valor_total_pedido(info_completa_pedido, quantidade_pedido)
    print("Valor total da compra: R$" + str(resultado))

    nome = input("Nome do cliente: ")
    telefone = input("Telefone do cliente: ")
    valido = verifica_telefone(telefone)
    while valido != True:
        print("Por favor, inserir um telefone válido para cadastro. ")
        telefone = input("Insira o número de telefone: ")
        valido = verifica_telefone(telefone)
    salva_pedido(info_completa_pedido, nome, telefone)

    print("Pedido: " + str(itens))
    print("Pedido finalizado")
    return True


#menu_pedidos()
   
    
