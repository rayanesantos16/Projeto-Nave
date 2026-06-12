#definir as váriavéis

combustivel =100
tripulantes = []

#definir funções

def viajar():
    global combustivel 
    if (len(tripulantes)==0):
        print(" Não á tripulantes")

    else:
        if (combustivel>=30):
            combustivel = combustivel - 30
            print("A nave viajou")
        else:
            print("Você não possui combustível suficiente para viajar. Abasteça!!")
    

def abastecer():
    global combustivel
    combustivel = 100
    print("Tanque cheio! 🛸")

def status_nave():
    #mostre a quantidade de combustível e os tripulantes
    print("\n-------------🧑‍🚀STATUS DA NAVE🧑‍🚀-------------")
    print(f"\nAtualmente, temos {combustivel} litros no tanque!")
    print(f"\nNossa tripulação é composta por: {tripulantes}\n")
    print("----------------------------------------\n")

def registrar_Tripulantes():
    novotripulante = input("qual é o nome do novo tripulante?")
    tripulantes.append(novotripulante)
    print("Novo tripulante inserido com sucesso!🚀")

def retirar_tripulantes():
    if retirar_tripulantes == "sim" and tripulantes != []:
        print(f"Nossa nave tem esses tripulantes: {tripulantes}")
        tripulantes.pop()
        print("Removendo ultimo tripulante")
    else:
         print(f"Nossa nave não tem  tripulantes")
         print ("Interação encerrada")

#criar um menu
print("Bem vindo ao menu interativo da nave. Por favor, selecione uma opçâo:")
while True:
    print("\n 1- Mostrar status da nave | 2- Viajar | 3- Abastecer | 4- Novo tribulante | 5- Retirar tripulante | 6- Sair")
    opção = input("Escolha: ")
    
    if opção == "1":
        status_nave()
    elif opção == "2":
        viajar()
    elif opção == "3":
     abastecer()
    elif opção == "4":
        registrar_Tripulantes()
    elif opção == "5":
        retirar_tripulantes()
    else:
        print("Viagem encerrada!")
        break




# viajar()
# viajar()
# viajar()
# viajar()
# abastecer()
# viajar()
# status_nave()


#POP() tira o ultimo elemento da listas