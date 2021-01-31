import os

def print_board(move):
    print('\n'*10)
    print(' '*54 + move[1] + ' |   ' + move[2] + '  | ' + move[3])
    print(' '*54 + '  |      |')
    print(' '*51 + "-----------------")
    print(' '*54 + move[4] + ' |   ' + move[5] + '  | ' + move[6])
    print(' '*54 + '  |      |')
    print(' '*51 + "-----------------")
    print(' '*54 + move[7] + ' |   ' + move[8] + '  | ' + move[9])
    print(' '*54 + '  |      |')

def turn(t,a,move):
    move[t]=a

def check_X(move):
    for i in range(1,8,3):
        if move[i]=="X" and move[i+1]=="X" and move[i+2]=="X":
            return 'winner is X'
    for j in range(1,4,1):
        if move[j]=="X" and move[j+3]=="X" and move[j+6]=="X":
            return "winner is X"
    for k in range(1,4,2):
        if k==1:
            if move[k]=="X" and move[k+4]=="X" and move[k+8]=="X":
                return "winner is X"
        else:
            if move[k]=="X" and move[k+2]=="X" and move[k+4]=="X":
                return 'winner is X'

def check_O(move):
    for i in range(1,8,3):
        if move[i]=="O" and move[i+1]=="O" and move[i+2]=="O":
            return 'winner is O'
    for j in range(1,4,1):
        if move[j]=="O" and move[j+3]=="O" and move[j+6]=="O":
            return "winner is O"
    for k in range(1,4,2):
        if k==1:
            if move[k]=="O" and move[k+4]=="O" and move[k+8]=="O":
                return "winner is O"
        else:
            if move[k]=="O" and move[k+2]=="O" and move[k+4]=="O":
                return 'winner is O'




move={1:" ",2:" ",3:" ",4:" ",5:" ",6:" ",7:" ",8:" ",9:" "}
print(" "*54 + "Welcome to the Tic Tac Toe Game")
print("\nEnter name :player 1")
player1=input()
os.system("cls")
print("\nEnter name :player 2")
player2=input()
os.system("cls")
print(" "*54 + 'Welcome ' + player1 + ' and '+ player2)
print(f'\n{player1} choose "X" or "O" ')
a11=input()
a1=a11.capitalize()
os.system("cls")
print(f'\n{player2} choose "X" or "O" ')
a22=input()
a2=a22.capitalize()
os.system("cls")
print_board(move)
#1
for _ in range(1,10,1):
    if _%2!=0:
        print('\n'*2 + " "*54 + f'{player1} your turn' + '\n'*2)
        t=int(input())
        turn(t,a1,move)
        os.system("cls")
        print_board(move)
        print('\n'*2)
        test=check_X(move)
        if test!=None:
            print(test)
            break

        
        
#2

    else:
        print('\n'*2 + f'{player2}''s turn' + '\n'*2)
        t=int(input())
        turn(t,a2,move)
        os.system("cls")
        print_board(move)
        print('\n'*2)
        test=check_O(move)
        if test!=None:
            print(test)
            break
print(" "*54 + "Game Overrrrrrr")
v=input()
