import os.path
import time
from collections import Counter

def pega_quantidade_pedidos(path_final_pedidos):
    quantidade = 0
    with open(path_final_pedidos, "r") as arquivo:
              arquivo = arquivo.readlines()
              for linha in arquivo:
                  if "R$" in linha:
                      quantidade += 1
    return int(quantidade)

def pega_quantidade_pedido_cliente(path_final_pedidos):
    pedidos_cliente = []
    quantidade = 0
    with open(path_final_pedidos, "r") as arquivo:
              arquivo = arquivo.readlines()
              for linha in arquivo:
                  pedidos_cliente.append(linha)
    return list(pedidos_cliente)

def quantidade_vendas_por_produto(path_final_pedidos):
    quantidade = 0
    n_produto = 0
    with open(path_final_pedidos, "r") as arquivo:
              arquivo = arquivo.readlines()
              for linha in arquivo:
                  quantidade += 1
                  if "R$" in linha:
                      produto = linha
                      for linha in arquivo:
                          if linha == produto and linha != quantidade:
                              n_produto += 1 
                              
                          else:
                              print("Já foi")                      
    return int(n_produto)

def duplicados(path_final_pedidos):
    lista = []
    duplicates = []
    rep = 0
    ind = 0
    i = 0
    with open(path_final_pedidos, "r") as arquivo:
              arquivo = arquivo.readlines()
              for linha in arquivo:
                  if "R$" in linha:
                      if linha in duplicates:
                          continue
                      else:
                          duplicates.append(linha)
                  else:
                        continue
              tamanho = len(duplicates)
              tamanho_fim = tamanho - 1
              indice = len(arquivo) - 1
              for item in duplicates:
                  for linha in arquivo:
                      if linha == duplicates[i]:
                          rep += 1
                          ind += 1
                      else:
                          ind += 1
                      if ind == indice:
                          novo = duplicates[i].replace("R$", "")
                          nova = novo.replace(novo[0:3], "")
                          nova_string = nova.split(",")
                          resultado = (nova_string[0] + " vendido até o momento: ",rep, )
                          lista.append(resultado)
                          i += 1
                          ind = 0
                          if i == tamanho_fim +1:
                              break
              return lista



def faturamento(path_final_pedidos):
    valor_vendas = []
    cont = 0
    with open(path_final_pedidos, "r") as arquivo:
              arquivo = arquivo.readlines()
              for linha in arquivo:
                  cont += 1
              if cont <= 1:
                  for pedido in arquivo:
                      if "R$" in pedido:
                          resultado = pedido.split('$')
                          valor = resultado[1]
                          return int(valor)
              else:
                  for pedido in arquivo:
                      if "R$" in pedido:
                          resultado = pedido.split("$")
                          valor_vendas.append(resultado[1])
                    
                  int_list = list(map(int, valor_vendas))
                  valor = sum(int_list)
              return int(valor)



  
                  
    

              

              
                      

              

      
                  
                            

                
    
    
