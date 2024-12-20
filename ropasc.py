import random

while True:
    # relating choices to emojis using dictionary
    # taking tuple cuz we dont need to modify choices
    choice = ('r','p','s')
    emojis={'r':'🪨','p':'📃','s':'✂️'}

    #taking the choice of the user and letting computer choose 
    user_choice = input('Rock, Paper or Scissor?!(r/p/s): ')
    comp_choice = random.choice(choice)
    if user_choice not in choice:
        print ('invalid response')

    #showing what the user chose and what the computer chose
    print (f'User chose: {emojis[user_choice]}')
    print (f'Computer chose: {emojis[comp_choice]}')

    #conditions for winning and loosing
    if (user_choice == 'r' and comp_choice == 's') or (user_choice == 's' and comp_choice == 'p') or (user_choice == 'p' and comp_choice == 'r'):
        print('you win')
    elif user_choice == comp_choice :
        print ('its a tie')
    else:
        print('you lost')
    cont = input ('Wanna play more? (y/n): ')
    if cont == 'n':
        print ('thanks for playing!')
        break