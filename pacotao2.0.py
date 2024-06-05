# eu vou fazer as funções
import os
import time


estoque = {}
nomes = []
preco = []
quantidade = []

def adicao():
    while True:
        produto = str(input("Digite o nome do produto:(aperte '0' para sair)\n"))
        if produto == '0':
                os.system('cls')
                break
        valor = int(input("Digite a quantidade do produto:"))
        estoque[produto] = valor
        print(estoque)
        time.sleep(1)
        os.system('cls')
        print(estoque)
def revisao():
    os.system('cls')
    for i in estoque.keys():
        print(i)
def exclusao():
    os.system('cls')
    print(estoque)
    produto = str(input('Digite o nome do produto que deseja excluir: (Para sair, pressione Enter)'))
    del estoque[produto]  
    exclusao()
def limpeza():
    os.system('cls')
    estoque.clear()
    print(estoque)
    time.sleep(1)
    os.system('cls')
def limpeza_lista():
    nomes.clear()
    preco.clear()
    quantidade.clear()
    print('lista limpa')
# def adicao_produto():
#     while True:
#         os.system('cls')
#         pnome = str(input('\nNome do produto:'))
#         if type(pnome) == str:
        
#             ppreco = int(input('\nPreço:'))
            
#             pquantidade = int(input('\nQuantidade:'))

#             preco.append(ppreco)
#             nomes.append(pnome)
#             quantidade.append(pquantidade)
#         else: 
#             break

def adicao_produto():
    
    while True:
        number = len(nomes) +1
        os.system('cls')
        pnome = (input(f'\nNome do {number}º produto:'))
        if pnome == '':
            os.system('cls')
            break
        else:
            ppreco = int(input('\nPreço:'))
                
            pquantidade = int(input('\nQuantidade:'))

            preco.append(ppreco)
            nomes.append(pnome)
            quantidade.append(pquantidade) 
            os.system('cls')
        
        
        
def revisao_produto():
    i = nomes.__len__()
    for i in range(i):
        
        total = preco[i] * quantidade[i]
    
        print(f'{i + 1}º  {quantidade[i]}x {nomes[i]} --- R${preco[i]} Total:{total}')
def exclusao_produto():
    while True:
        if nomes == []:
            os.system('cls')
            print('lista vazia')
            time.sleep(1)
            os.system('cls')
            break
        else:
            os.system('cls')
            print(revisao_produto())
            opcao = int(input('digite o nº do produto que deseja excluir'))
            topcao = type(opcao)
            if topcao == int: 
                print(f'{nomes[opcao - 1]} excluido')
                time.sleep(0.5)
                del nomes[opcao - 1]
                del preco[opcao - 1]
                del quantidade[opcao - 1] 
            else:
                break


while True:
    try:
        menu = int(input('\nBem vindo(a) ao PaCoTãO\n Seu estoque online\n\n Digite:\n (1) Para adicionar um produto\n (2) Para revisar seu estoque\n (3) Para remover algum produto\n (4) Para limpar o estoque \n(0) Para sair\n-->'))

        if menu == 1:
            # adicao()
            adicao_produto()
        elif menu == 2:
            revisao()
            if nomes.__len__() == 0:
                         
                os.system('cls')
                print('O estoque está vazio\n\n\n')
                
                time.sleep(1)
                input("...pressione enter.")
            else:
                os.system('cls')
                revisao_produto()
                
                time.sleep(2)
                input("pressione enter")
    
        elif menu == 3:
            # exclusao()
            exclusao_produto()
        elif menu == 4:
            cert = input("tem certeza? Digite 's' ")
            if cert == "s":
                nomes.clear()
                preco.clear()
                quantidade.clear()
                print("Estoque limpo")
                time.sleep(0.5)
                os.system('cls')
            else: print('ação não confirmada')
            
        elif menu == 0:
            os.system('cls')
            print('Obrigado por usar o PaCoTãO')
            time.sleep(1)
            break
        elif menu == 9:
            nomes  = ["nome1", "nome2", "nome3", "nome4", "nome5", "nome6"]
            preco = [10, 20, 30, 40, 50, 60]
            quantidade = [10, 20, 30, 40, 50, 60]
            os.system('cls')
            print("lista teste pronta")

    except ValueError:
        print('por favor, digite apenas números')
        os.system('cls')
    except TypeError:
        print('type errssos')   
        os.system('cls')
    except NameError:
        print('name error')
        os.system('cls')
    except KeyError:
        print("não existe esse produto ou o estoque está vazio")
        os.system('cls')
        time.sleep(1)