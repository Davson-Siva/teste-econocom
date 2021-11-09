from func_clientes import *
from func_pedidos import *
from pedidos import *
#from main import *

                              
dir_path = os.path.dirname(os.path.realpath(__file__))
path_final_clientes = dir_path + str("\clientes.txt")                       
                      

def menu_clientes():
    print("SISTEMA DE ATENDIMENTO Lanches da Quarentena.")

    acao = input("1 = Realizar novo pedido \n2 = Deletar Cliente \n3 = Editar cliente \n4 = Cadastrar Cliente \n")
    while acao != "1" and acao != "2" and acao != "3" and acao != "4":
        print("Opção inválida. Digite '1', '2' ou '3' ´para continuar. ")
        acao = input("1 = Realizar novo pedido \n2 = Deletar Cliente \n3 = Editar cliente ")


    if acao == "2":
        continuar = "y"
        while continuar == "y":
            nome = input("Digite o nome do cliente: ")
            telefone = input("Digite o telefone do cliente")
            valido = verifica_telefone(telefone)
            while valido != True:
                print("Por favor, inserir um telefone válido para cadastro. ")
                telefone = input("Insira o número de telefone: ")
                valido = verifica_telefone(telefone)

            existe = verifica_cliente_ja_existe(nome, telefone)

            if existe == False:
                if(remove_cliente(nome, telefone)):
                    print("Cliente removido")
                    continuar = input("Deseja remover mais clientes do sistema? Y/N ")
                    while continuar.lower() != "y" and continuar.lower() != "n":
                        print("OPÇÃO INVÁLIDA!")
                    continuar = input("Deseja remover mais clientes do sistema? Y/N ")
                    if continuar == "y":
                        continue
                    else:
                        return True
        else:
            print("Cliente não encontrado no arquivo.")
            return True
            
            

    elif acao == "3":
        continuar = "y"
        while continuar == "y":
            nome = input("Digite o nome do cliente para edição: ")
            telefone_antigo = input("Digite o telefone antigo do cliente")
            novo_telefone = input("Digite o novo telefone do cliente")
            valido_telefone_antigo = verifica_telefone(telefone_antigo)
            while valido_telefone_antigo != True:
                print("Por favor, inserir um telefone válido para cadastro. ")
                telefone = input("Insira o número de telefone: ")
                valido = verifica_telefone(telefone_antigo)

            valida_novo_telefone = verifica_telefone(novo_telefone)
            while valida_novo_telefone != True:
                print("Por favor, inserir um telefone válido para cadastro. ")
                telefone = input("Insira o número de telefone: ")
                valido = verifica_telefone(novo_telefone)

            existe = verifica_cliente_ja_existe(nome, telefone_antigo)

            if existe == False:
                
                if(edita_cliente(nome, novo_telefone, telefone_antigo)):
                    print("Cadastro alterado com sucesso.")
                    continuar = input("Deseja editar outro cadastro? Y/N ")
                    while continuar.lower() != "y" and continuar.lower() != "n":
                        print("OPÇÃO INVÁLIDA")
                        continuar = input("Deseja editar outro cadastro? Y/N ")
                    if continuar == "y":
                        continue
                    else:
                        return True
                        
                else:
                    print("Falha ao editar cliente")
                    continuar = input("Deseja editar outro cadastro? Y/N ")
                    while continuar.lower() != "y" and continuar.lower() != "n":
                        print("OPÇÃO INVÁLIDA")
                        continuar = input("Deseja editar outro cadastro? Y/N ")
                    if continuar == "y":
                        continue
                    else:
                        return True
            else:
                print("Cliente não encontrado no arquivo.")
                continuar = input("Deseja editar outro cadastro? Y/N ")
                while continuar.lower() != "y" and continuar.lower() != "n":
                    print("OPÇÃO INVÁLIDA")
                    continuar = input("Deseja editar outro cadastro? Y/N ")
                if continuar == "y":
                    continue
                else:
                    return True

    
    elif acao == "1":
        continuar = "y"
        while continuar == "y":
            cliente = input("Já é cliente da loja? Y/N ")

            while cliente.lower() != "y" and cliente.lower() != "n":
                print("Opção inválida. Digite 'Sim' ou 'Nao' ´para continuar. ")
                cliente = input("Para darmos início, o sr(a) já é cliente? ")

            if cliente.lower() == "y":
                print("Vamos iniciar seu pedido")
                if(menu_pedidos()):
                    continuar = input("Deseja realizar mais pedidos? Y/N ")
                    while continuar.lower() != "y" and continuar.lower() != "n":
                        print("OPÇÃO INVÁLIDA!")
                        continuar = input("Deseja realizar mais pedidos? Y/N ")

                    if continuar == "y":
                        continue
                    else:
                        return True

            if cliente.lower() == "n":
                print("Vamos iniciar o cadastro.")
                nome = input("Insira o primeiro nome: ")
                telefone = input("Insira o número de telefone: ")
                valido = verifica_telefone(telefone)
                while valido != True:
                    print("Por favor, inserir um telefone válido para cadastro. ")
                    telefone = input("Insira o número de telefone: ")
                    valido = verifica_telefone(telefone)
                if(verifica_arquivo_txt()):
                    existe = verifica_cliente_ja_existe(nome, telefone)

                    while existe == False:
                        seguir = input("Identificamos em nosso sistema que já possui um cadastro com esses dados. Deseja utilizar esse cadastro? Y/N")
                        while seguir.lower() != "y" and seguir.lower() != "n":
                            seguir = input("Opção inválida. Digite 'Y' ou 'N' ´para continuar. ")

                        if seguir.lower() == "y":
                            print("Vamos iniciar seu pedido")
                            if(menu_pedidos()):
                                continuar = input("Deseja realizar mais pedidos? Y/N ")
                                while continuar.lower() != "y" and continuar.lower() != "n":
                                    print("OPÇÃO INVÁLIDA!")
                                    continuar = input("Deseja realizar mais pedidos? Y/N ")

                                if continuar == "y":
                                    continue
                                else:
                                    return True
                            
                        if continuar.lower() == "n":
                            print("Vamos iniciar o cadastro")
                            nome = input("Insira o primeiro nome: ")
                            telefone = input("Insira o número de telefone: ")
                            valido = verifica_telefone(telefone)
                            while valido != True:
                                print("Por favor, inserir um telefone válido para cadastro. ")
                                telefone = input("Insira o número de telefone: ")
                                valido = verifica_telefone(telefone)
                            existe = verifica_cliente_ja_existe(nome, telefone)
                        
                  
                if(cadastra_cliente(nome, telefone)):
                    print("Cadastro realizado com sucesso.")
                    print("Vamos iniciar o pedido.")
                    if(menu_pedidos()):
                        s
                        continuar = input("Deseja realizar mais pedidos? Y/N ")
                        while continuar.lower() != "y" and continuar.lower() != "n":
                            print("OPÇÃO INVÁLIDA!")
                            continuar = input("Deseja realizar mais pedidos? Y/N ")

                        if continuar == "y":
                                continue
                        else:
                            return True
                else:
                    print("Falha ao cadastrar cliente")
                    continuar = input("Deseja continuar novamente? Y/N ")
                    while continuar.lower() != "y" and continuar.lower() != "n":
                        print("OPÇÃO INVÁLIDA!")
                        continuar = input("Deseja realizar mais pedidos? Y/N ")

                    if continuar == "y":
                        continue
                    else:
                        return True


    elif acao == "4":
        continuar = "y"
        while continuar == "y":
            print("Vamos iniciar o cadastro.")
            nome = input("Insira o primeiro nome: ")
            telefone = input("Insira o número de telefone: ")
            valido = verifica_telefone(telefone)
            while valido != True:
                print("Por favor, inserir um telefone válido para cadastro. ")
                telefone = input("Insira o número de telefone: ")
                valido = verifica_telefone(telefone)
            if(verifica_arquivo_txt()):
                existe = verifica_cliente_ja_existe(nome, telefone)
                print("existe: " + str(existe))

                while existe == False:
                    continuar = input("Identificamos em nosso sistema que já possui um cadastro com esses dados. Deseja utilizar esse cadastro? Y/N")
                    while continuar.lower() != "y" and continuar.lower() != "n":
                        continuar = input("Opção inválida. Digite 'Y' ou 'N' ´para continuar. ")

                if(cadastra_cliente(nome, telefone)):
                    print("Cadastro realizado com sucesso.")
                    continuar = input("Deseja cadastrar mais clientes? Y/N ")
                    while continuar.lower() != "y" and continuar.lower() != "n":
                        print("OPÇÃO INVÁLIDA!")
                        continuar = input("Deseja realizar mais pedidos? Y/N ")

                    if continuar == "y":
                        continue
                    else:
                        return True
                else:
                    print("Falha ao cadastrar cliente")
                    continuar = input("Deseja continuar novamente? Y/N ")
                    while continuar.lower() != "y" and continuar.lower() != "n":
                        print("OPÇÃO INVÁLIDA!")
                        continuar = input("Deseja realizar mais pedidos? Y/N ")

                    if continuar == "y":
                        continue
                    else:
                        return True

        

            

#menu_clientes()
