from pedidos import *
from relatorio import *
from produtos import *
from clientes import *

def menu_main():
    
    print("SISTEMA DE ATENDIMENTO LANCHES DA QUARENTENA")
    print("MENUS DE ACESSO: ")

    menu = input("1 = INICIAR PEDIDO \n2 = PRODUTOS DO CARDÁPIO \n3 = STATUS\RELATÓRIOS \n4 = CLIENTES \n")
    while menu.lower() != "1" and menu.lower() != "2" and menu.lower() != "3" and menu.lower() != "4":
        print("Opção inválida. Por favor, digitar '1', '2' ou '3' para indicar qual menu acessar.")
        menu = input("1 = PEDIDOS \n2 = PRODUTOS DO CARDÁPIO \n3 = STATUS\RELATÓRIOS")

    if menu == "1":
        if(menu_pedidos()):
            sair = input(str("Deseja encerrar o sistema? Y/N "))
            while sair.lower() != "y" and sair.lower() != "n":
                print("OPÇÃO INVÁLIDA.")
                sair = input(str("Deseja encerrar o sistema? Y/N "))
            return str(sair)
    elif menu == "2":
        if(menu_produtos()):
            sair = input(str("Deseja encerrar o sistema? Y/N "))
            while sair.lower() != "y" and sair.lower() != "n":
                print("OPÇÃO INVÁLIDA.")
                sair = input(str("Deseja encerrar o sistema? Y/N "))
            return str(sair)
            
    elif menu == "3":
        if(menu_relatorios()):
            sair = input(str("Deseja encerrar o sistema? Y/N "))
            while sair.lower() != "y" and sair.lower() != "n":
                print("OPÇÃO INVÁLIDA.")
                sair = input(str("Deseja encerrar o sistema? Y/N "))
            print("vamos sair? ", sair)
            return str(sair)
            
    elif menu == "4":
        if(menu_clientes()):
            sair = input(str("Deseja encerrar o sistema? Y/N "))
            while sair.lower() != "y" and sair.lower() != "n":
                print("OPÇÃO INVÁLIDA.")
                sair = input(str("Deseja encerrar o sistema? Y/N "))
            print("vamos sair? ", sair)
            return str(sair)
