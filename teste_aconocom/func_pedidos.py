import os.path
import time

dir_path = os.path.dirname(os.path.realpath(__file__))
path_final_produtos = dir_path + str("\produtos.txt")
path_final_pedidos = dir_path + str("\pedidos.txt")


def pega_lista_produtos(path_final_produtos):
    with open(path_final_produtos, "r") as arquivo:
              arquivo = arquivo.readlines()
              for linha in arquivo:
                  print(linha)
    return True

def escolhe_pedido(codigo_produto):
    pedido = []
    for codigo in codigo_produto:
        with open(path_final_produtos, "r") as arquivo:
              arquivo = arquivo.readlines()
              for linha in arquivo:
                  if codigo in linha:
                      pedido.append(codigo)

def verifica_codigo_pedido(item):
    with open(path_final_produtos, "r") as arquivo:
        arquivo = arquivo.readlines()
        for linha in arquivo:
            if linha[0:1]== item:
                return True


    return False

def informacao_completa_pedido(lista_pedido:list, quantidade_pedido):
    print("func: ", quantidade_pedido)
    cont = 0
    info_pedido = []
    while cont <= quantidade_pedido:
        for pedido in lista_pedido:
            with open(path_final_produtos, "r") as arquivo:
                arquivo = arquivo.readlines()
                for linha in arquivo:
                    
                    if linha[0:1]== pedido:
                        info_pedido.append(linha)
                        cont += 1
                        print("cont: ", cont)
                        if cont == quantidade_pedido:
                            return info_pedido
                            
                        

            
    

def adiciona_pedido_na_lista(pedido, lista_pedido:list):
    try:
        lista_pedido.append(pedido)
        return lista_pedido
    except:
        return False

def remove_item_pedido(pedido_completo, item_para_excluir=str):
    for pedido in pedido_completo:
        if item_para_excluir in str(pedido):
            pedido_completo.remove(item_para_excluir)
            return True
    return False

def pega_quantidade_pedido_atual(lista_pedido:list):
    quantidade = 0
    for pedido in lista_pedido:
        quantidade += 1

    return int(quantidade)

def salva_pedido(lista_pedido:list, nome, telefone):
    print("lista ", lista_pedido)
    with open(path_final_pedidos, "a") as arquivo:
            arquivo.write(str("Cliente: " + str(nome)) + " Telefone: " + str(telefone) + '\n')
    for pedido in lista_pedido:
        print(pedido)
        with open(path_final_pedidos, "a") as arquivo:
            arquivo.write(str(pedido) + '\n')
    return True

def valor_total_pedido(lista_pedido:list, quantidade_pedido:int):
    valor_pedido = []
    if quantidade_pedido <= 1:
        for pedido in lista_pedido:
            resultado = pedido.split('$')
            valor = resultado[1]
            return int(valor)
    else:
        for pedido in lista_pedido:
            resultado = pedido.split('$')
            valor_pedido.append(resultado[1])

        int_list = list(map(int, valor_pedido))
        valor = sum(int_list)
    return int(valor)
