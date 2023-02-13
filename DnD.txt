print('''

     _                                                      _       _                                 
    | |                                                    | |     | |                                
  __| |_   _ _ __   __ _  ___  ___  _ __     __ _ _ __   __| |   __| |_ __ __ _  __ _  ___  _ __  ___ 
 / _` | | | | '_ \ / _` |/ _ \/ _ \| '_ \   / _` | '_ \ / _` |  / _` | '__/ _` |/ _` |/ _ \| '_ \/ __|
| (_| | |_| | | | | (_| |  __/ (_) | | | | | (_| | | | | (_| | | (_| | | | (_| | (_| | (_) | | | \__ \
 \__,_|\__,_|_| |_|\__, |\___|\___/|_| |_|  \__,_|_| |_|\__,_|  \__,_|_|  \__,_|\__, |\___/|_| |_|___/
                    __/ |                                                        __/ |                
                   |___/                                                        |___/                 

''')
print('Welcome to Dungeons & Dragons')

player_name = input('What is your name, adventurer?\n')

health = 100
damage = 20

print('\nWelcome, ' + player_name + '! You have ' + str(health) + ' health and can do damage ' + str(damage))
print('You came across a dragon, what will you do?')
print('1. Fight')
print('2. Run')

choice = int(input('\nEnter either 1 or 2 : '))
if choice == 1 :
    print('You attack the dragon and deals ' + str(damage) + 'damage towards it')
    print('The dragon back off, spit some acid and does 10 damage') 
    health = 10
    print('Your current health is ' + str(health)) 
elif choice == 2 : 
    print('You run away from the dragon') 
    print('Live today for tomorrow') 
    print('\nOh no, Dragon manages to throw rocks at you and deals with twice the damage you inflict!')
    print('Your current health is = ' + str(health-40))
else: 
    print('\nInvalid choice, the dragon get to eat you alive!!!') 
print("\nThanks for playing!")