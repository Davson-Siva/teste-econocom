import os.path

dir_path = os.path.dirname(os.path.realpath(__file__))
path_final_produtos = dir_path + str("\produtos.txt")

def pega_lista_produtos(path_final_produtos):
    with open(path_final_produtos, "r") as arquivo:
              arquivo = arquivo.readlines()
              for linha in arquivo:
                  print(linha)
    return True


def verifica_codigo_pedido(item):
    with open(path_final_produtos, "r") as arquivo:
        arquivo = arquivo.readlines()
        for linha in arquivo:
            if linha[0:1]== item:
                return True


    return False

def edita_nome_produto(produto, novo_nome, path_final_produtos):
    lista_produtos = []
    valor = "R$20"
    #dados = str(nome) + ":" + str(telefone_antigo)
    with open(path_final_produtos, "r+") as arquivo:
        arquivo = arquivo.readlines()
        for linha in arquivo:
            lista_produtos.append(linha)
            

        for item in lista_produtos:
            if produto in str(item):
                try:
                    lista_produtos.remove(item)
                    lista_produtos.append("\n" + str(produto) + " = " + str(novo_nome) + ", " + str(valor))
                    with open(path_final_produtos, "w") as arquivo:
                        for item in lista_produtos:
                            arquivo.write(str(item))
                    return True
                except:
                    return False

def adiciona_produto(path_final_produtos, nome_produto, valor_produto:str):
    lista_produtos = []
    valor = "R$" + str(valor_produto)
    
    #dados = str(nome) + ":" + str(telefone_antigo)
    with open(path_final_produtos, "r+") as arquivo:
        arquivo = arquivo.readlines()
        for linha in arquivo:
            lista_produtos.append(linha)
        indice = len(lista_produtos) - 1
        codigo = indice + 1
        lista_produtos.append("\n" + str(codigo) + " = " + str(nome_produto) + ", " + str(valor))
        try:
            with open(path_final_produtos, "w") as arquivo:
                for item in lista_produtos:
                    arquivo.write(str(item))
                return True
        except:
            return False


def remove_produto(path_final_produtos, produto:str):
    lista_produtos = []
    #dados = str(nome) + ":" + str(telefone)
    with open(path_final_produtos, "r+") as arquivo:
              arquivo = arquivo.readlines()
              for linha in arquivo:
                  lista_produtos.append(linha)

              for item in lista_produtos:
                  if produto in str(item):
                      lista_produtos.remove(item)
                      with open(path_final_produtos, "w") as arquivo:
                          for item in lista_produtos:
                              arquivo.write(str(item))
                          return True

def verifica_codigo_pedido(item):
    with open(path_final_produtos, "r") as arquivo:
        arquivo = arquivo.readlines()
        for linha in arquivo:
            if linha[0:1]== item:
                return True

        return False
    





    
