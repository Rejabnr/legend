import random
print("*******************************")
print("Welcome to the Caveman Battle !")
print("*******************************")

player1_name = input("Player 1, what is your name?")

player2_name = input("Player 2, what is your name?")

player1_health = 100
player1_ammo = 50
player1_damage = 20

player2_health = 122
player2_ammo = 52
player2_damage = 22

print("\n" + player1_name + " has " + str(player1_health) + " health, " + str(player1_ammo) + " rounds of ammo and " + str(player1_damage) + " damage")
print("\n" + player2_name + " has " + str(player2_health) + " health, " + str(player2_ammo) + " rounds of ammo and " + str(player2_damage) + " damage")

print("\nYour cave is suddenly attacked by wild animals. What will you do?")
print('1.Fight')
print('2.Run')
print('3.Search for supplies')

player1_choice = int(input('\nWhat would player 1 do in this situation?'))

if player1_choice == 1 :
    print('Player 1 fights the wild animals and does' + str(player1_damage) + 'damages!')
    player1_ammo -=10
    if player1_ammo >0 :
        print('\n' + player1_name + ' defeated the animals!! They have ' + str(player1_ammo) + ' ammo left')

elif player1_choice == 2 :
    print('Lived to fight another day ...')
    print('The animals manage to chase them out')
    print('\nOh no, the animals had bitten player 2!')
    player2_health -= 100
    print('Player 2 health is = ' + str(player2_health))
    print('\nThe animals suddenly attacked player 1 and did some critical damages towards them!')
    player1_health -= 50
    print(player1_name + 's health left is ' + str(player1_health))

elif player1_choice == 3 :
    random_number = random.randint(1,20) 
    print(random_number) 
    if random_number > 5 : 
        print("They manage to save some foods") 
    elif random_number : 
        print("They manage to ran away with their cloths")
    elif random_number :
        print("They manage to get some weapons")
    elif random_number :
        print("They get some helps from other caveman")
    else :
        print("They get no loot")

else :
    print('Invalid input, sad day for the caveman')