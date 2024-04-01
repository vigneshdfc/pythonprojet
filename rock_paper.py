import random

def play():
    user = input("Whats your choise? 'r' for rock,'p' for paper,'s' for scissors " )
    print(user)
    computer =random.choice(['r','p','s'])
    print(computer)

    if user == computer:
        return "It's tie"

    if is_win(user,computer):
        return 'You won!'
    return 'You lost'


def is_win(player,opponent):
    if(player == 'r' and opponent =='s')or(player == 's' and opponent =='p')or(player == 'p' and opponent =='r'):
        return True


print(play())