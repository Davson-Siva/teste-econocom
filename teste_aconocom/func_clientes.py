import os.path

dir_path = os.path.dirname(os.path.realpath(__file__))
path_final_clientes = dir_path + str("\clientes.txt")


#print(os.path.dirname(os.path.realpath(__file__)))

def cadastra_cliente(nome, telefone):
    print("Nome do cliente: " + str(nome))
    print("Telefone do cliente: " + str(telefone))
    dados = str(nome) + ":" + str(telefone)
    with open(path_final_clientes, "a") as arquivo:
        arquivo.write(str(dados) + '\n')
        return True


def verifica_arquivo_txt():
    return os.path.isfile("clientes.txt")


def verifica_telefone(telefone):
    if (len(telefone) < 8 or len(telefone) > 9):
        return False
    return True

def verifica_cliente_ja_existe(nome, telefone):
    dados = str(nome) + ":" + str(telefone)
    with open(path_final_clientes, "r") as arquivo:
              arquivo = arquivo.readlines()
              for linha in arquivo:
                  if(dados in linha):
                      return False
    return True

def remove_cliente(nome, telefone):
    lista_clientes = []
    dados = str(nome) + ":" + str(telefone)
    with open(path_final_clientes, "r+") as arquivo:
              arquivo = arquivo.readlines()
              for linha in arquivo:
                  print(linha)
                  lista_clientes.append(linha)
                  print("ADICIONADO: " + str(lista_clientes))

              for cliente in lista_clientes:
                  if dados in str(cliente):
                      lista_clientes.remove(cliente)
                      with open(path_final_clientes, "w") as arquivo:
                          for cliente in lista_clientes:
                              
                              arquivo.write(str(cliente))
                          return True
def edita_cliente(nome, novo_telefone, telefone_antigo):
    lista_clientes = []
    dados = str(nome) + ":" + str(telefone_antigo)
    with open(path_final_clientes, "r+") as arquivo:
        arquivo = arquivo.readlines()
        for linha in arquivo:
            lista_clientes.append(linha)
            

        for cliente in lista_clientes:
            if dados in str(cliente):
                try:
                    lista_clientes.remove(cliente)
                    lista_clientes.append(str(nome) + ":" + str(novo_telefone))
                    with open(path_final_clientes, "w") as arquivo:
                        for cliente in lista_clientes:
                            arquivo.write(str(cliente))
                    return True
                except:
                    return False
