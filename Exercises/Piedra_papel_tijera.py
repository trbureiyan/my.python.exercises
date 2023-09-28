import random

print("\n")

print("Bienvenido a Piedra Papel Tijera")

print("\n")

options = ("piedra", "papel", "tijera")

Player1_wins = 0
Computer_wins = 0

rounds = 1

while True:

    print("-" * 20)
    print("Ronda numero ", rounds)
    print("-" * 20)
    
    print("\n")
    
    elecc_user1 = input("Por favor ingrese su eleccion => ").lower()
    elecc_pc1 = random.choice(options)

    print("\n")

    if elecc_user1 == 'piedra':
        print("Player1 elige 🪨 ", elecc_user1)
    elif elecc_user1 == 'papel':
        print("Player1 elige 📄 ", elecc_user1)
    elif elecc_user1 == 'tijera':
        print("Player1 elige ✂️ ", elecc_user1)
    else:
        print("Hubo un error, elige piedra, papel o tijera")
        exit()

    print("Computer elige", elecc_pc1)

    print("\n")

    if elecc_user1 == elecc_pc1:
            print('Empate!')
    elif elecc_user1 == 'piedra':
            if elecc_pc1 == 'tijera':
            # print('piedra gana a tijera')
                print('Player1 ganó!')
                Player1_wins += 1

            else:
            #  print('Papel gana a piedra')
                print('Computer ganó!')
                Computer_wins += 1

    elif elecc_user1 == 'papel':
            if elecc_pc1 == 'piedra':
            #  print('papel gana a piedra')
                print('Player1 ganó')
                Player1_wins += 1

            else:
            #  print('tijera gana a papel')
                print('computer ganó!')
                Computer_wins += 1

    elif elecc_user1 == 'tijera':
            if elecc_pc1 == 'papel':
            #   print('tijera gana a papel')
                print('Player1 ganó!')
                Player1_wins += 1

            else:
            #  print('piedra gana a tijera')
                print('computer ganó!')
                Computer_wins += 1
    
    print("\n")


    if Player1_wins > 2:
        break
    if Computer_wins > 2:
        break
    
    rounds += 1
    
    if Player1_wins == 1:
        print("Player1 ha ganado ", Player1_wins, " vez")
    else: 
        print("Player1 ha ganado ", Player1_wins, " veces")
        
    if Computer_wins == 1:
        print("Computer ha ganado ", Computer_wins, " vez")
    else: 
        print("Computer ha ganado ", Computer_wins, " veces")
    
    print("\n")

'''

Author: @trbureiyan :)

'''
