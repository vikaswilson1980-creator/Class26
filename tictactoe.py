board = {'7':'','8':'','9':'','4':'','5':'','6':'','1':'','2':'','3':'',}
board_keys = []
for key in board:
    board_keys.append(key)
def printboard(board):
    print(board['7']+'|'+board['8']+'|'+board['9'])
    print('-+-+-')
    print(board['4']+'|'+board['5']+'|'+board['6'])
    print('-+-+-')
    print(board['1']+'|'+board['2']+'|'+board['3'])
def game():
    turn = 'X'
    count = 0
    for i in range(10):
        printboard(board)
        print("It is your turn"+turn+"Move to which place")
        move = input()
        if board[move]==' ':
            board[move]=turn
            count+=1
        else:
            print("The place is already filled move to which place. Continue")
        if count >=5:
            if board['7']== board['8'] == board['9']!= ' ': #Across the top
                printboard(board)
                print("Game over")
                print("****"+turn+"Won")
                break
            elif board['4']== board['5'] == board['6']!= ' ': #Across the middle
                printboard(board)
                print("Game over")
                print("****"+turn+"Won")
                break
            elif board['1']== board['2'] == board['3']!= ' ': #Across the bottom
                printboard(board)
                print("Game over")
                print("****"+turn+"Won")
                break
            elif board['1']== board['4'] == board['7']!= ' ': #Down the left side
                printboard(board)
                print("Game over")
                print("****"+turn+"Won")
                break
            elif board['2']== board['5'] == board['8']!= ' ': #Down the middle
                printboard(board)
                print("Game over")
                print("****"+turn+"Won")
                break
            elif board['3']== board['6'] == board['9']!= ' ': #Down the right side
                printboard(board)
                print("Game over")
                print("****"+turn+"Won")
                break
            elif board['7']== board['5'] == board['3']!= ' ': #diagonal
                printboard(board)
                print("Game over")
                print("****"+turn+"Won")
                break
            elif board['1']== board['5'] == board['9']!= ' ': #diagonal
                printboard(board)
                print("Game over")
                print("****"+turn+"Won")
                break
        if count == 9:
            print("Game over")
            print("Its a tie")
        if turn == 'X':
            turn='O'
        else:
            turn = 'X'
restart = input("Do you want to play again(Yes/No)")
if restart == 'Yes' or restart == 'yes':
    for key in board_keys:
        board[key]= ' '
    game()
if __name__=="__main__":
    game()