import random

# taking tuple cuz we dont need to modify choices
emojis = {'r':'🪨','p':'📃','s':'✂️'}
choice = tuple(emojis.keys()) #basically this will make a tuple of the key values of the emoji tuple.

#taking the choice of the user and letting computer choose 
def get_user_choice ():
    while True:    
        user_choice = input('Rock, Paper or Scissor?!(r/p/s): ')
        comp_choice = random.choice(choice)
        if user_choice in choice:
            return user_choice
        else: 
            print ('invalid response')
    

#showing what the user chose and what the computer chose
def disp_user_choice(user_choice, comp_choice):
    print (f'User chose: {emojis[user_choice]}')
    print (f'Computer chose: {emojis[comp_choice]}')

#conditions for winning and loosing
def det_winner(user_choice, comp_choice):
    if (user_choice == 'r' and comp_choice == 's') or (user_choice == 's' and comp_choice == 'p') or (user_choice == 'p' and comp_choice == 'r'):
        print('you win')
    elif user_choice == comp_choice :
        print ('its a tie')
    else:
        print('you lost')

#refactoring code and making it modular
def play_game():
    while True :
        user_choice = get_user_choice()
        comp_choice = random.choice(choice)
        disp_user_choice(user_choice,comp_choice)
        det_winner(user_choice,comp_choice)
        cont = input ('Wanna play more? (y/n): ')
        if cont == 'n':
            print ('thanks for playing!')
            break
        

play_game()
