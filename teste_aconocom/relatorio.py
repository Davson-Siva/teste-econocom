import os.path
import time
from collections import Counter
from func_relatorio import *
dir_path = os.path.dirname(os.path.realpath(__file__))
path_final_pedidos = dir_path + str("\pedidos.txt")
path_final_produtos = dir_path + str("\produtos.txt")


def menu_relatorios():
    continuar = "n"
    while continuar == "n":
        resultado = faturamento(path_final_pedidos)
        print("Faturamento até o momento: ", resultado)

        resultado = pega_quantidade_pedidos(path_final_pedidos)
        print("\nQuantidade de Pedidos até o momento: " + str(resultado))


        pedidos_até_momento = pega_quantidade_pedido_cliente(path_final_pedidos)
        print("\nPEDIDOS POR CADA CLIENTE:")
        for pedido in pedidos_até_momento:
            print(pedido)

        resultado = duplicados(path_final_pedidos)

        print("Vendas por produto: ")
        for linha in resultado:
            print(linha)


        continuar = input("Deseja encerrar a consulta? Y/N ")
        while continuar.lower() != "y" and continuar.lower() != "n":
            print("OPÇÃO INVÁLIDA!")
            continuar = input("Deseja encerrar a consulta? Y/N ")

        if continuar == "y":
            return True

        else:
            continue
        

