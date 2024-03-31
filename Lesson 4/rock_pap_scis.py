import random

ROCK = 'rock'
PAPER = 'paper'
SCISSORS ='scissors'

def get_computer_rps():
    random_int = random.randint(1,3)
    if random_int == 1:
        return ROCK
    if random_int == 2:
        return PAPER
    return SCISSORS

def get_user_rps():
    user = ''
    while user != ROCK and user != PAPER and user != SCISSORS:
        user = input('Enter rock, paper, or scissors: ')
    return user

def result_check(user, computer):
    if user == computer:
        print('TIE')
    elif (user == PAPER and computer == ROCK) or \
         (user == ROCK and computer == SCISSORS) or \
         (user == SCISSORS and computer == PAPER):
        print('USER WON')
    else:
        print('COMPUTER WON')


def main():
    user_choice = get_user_rps()
    computer_choice = get_computer_rps()
    print('Computer choice : ' + computer_choice)
    result_check(user_choice, computer_choice)
main()
  
   
 
