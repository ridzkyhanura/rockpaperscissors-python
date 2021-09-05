import random

def print_hand(hand, name):
    hands = ['Rock', 'Paper', 'Scissors']
    return print(name + ' choose ' + hands[hand - 1])
    
def judge(player_hand, com_hand):
    if player_hand == 1 and com_hand == 2:
        return 'Lose'
    elif player_hand == 2 and com_hand == 3:
        return 'Lose'
    elif player_hand == 3 and com_hand == 1:
        return 'Lose'
    elif player_hand == com_hand:
        return 'Draw'
    else:
        return 'Win'

print('===============================')
print('Rock Paper Scissors Game')
print('By: ridzkyhanura')
print('===============================')
print('')
ongame = 1
player_score = 0
com_score = 0
numofgames = 0
player_name = input('What is your name?: ')
if player_name == '':
    player_name = 'Guest'
else:
    pass
while ongame == 1:
    handmenu = 1
    numofgames += 1
    while handmenu == 1:
        print('')
        print('Choose hand:')
        print('1. Rock')
        print('2. Paper')
        print('3. Scissors')
        print('')
        player_hand = input('Input a number (1-3): ')
        if player_hand == '1' or player_hand == '2' or player_hand == '3':
            handmenu = 0
        else:
            print('Your input must be number 1 or 2 or 3!')
    computer_hand = random.randint(1,3)
    print_hand(int(player_hand), player_name)
    print_hand(computer_hand, 'Computer')
    print('')
    result = judge(int(player_hand), computer_hand)
    if result == 'Win':
        player_score += 1
    elif result == 'Lose':
        com_score += 1
    else:
        pass
    print(player_name + ' ' + result)
    print('Score ' + player_name + ' VS Computer: ' + str(player_score) + ' - ' + str(com_score))
    print('')
    continuemenu = 1
    while continuemenu == 1:
        continu = input('Are you still want to play again? (Y/N): ')
        if continu == 'Y' or continu == 'y':
            continuemenu = 0
        elif continu == 'N' or continu == 'n':
            continuemenu = 0
            ongame = 0
        else:
            print('Your input must be Y or N!')
            print('')
print('')
print('Statistics:')
print('Number of games: ' + str(numofgames) + ' times')
print('Final score ' + player_name + ' VS Computer: ' + str(player_score) + ' - ' + str(com_score))
print('')
print(player_name + ' ends the game')    
