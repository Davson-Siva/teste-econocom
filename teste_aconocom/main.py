from pedidos import *
from relatorio import *
from produtos import *
from clientes import *
from func_main import *


sair = "n"
while sair == "n":
    if(menu_main() == "y"):
        print("SISTEMA ENCERRADO")
        sair = "y"
