board = list(range(1,10))
def draw_board(board):
    print(" 1 2 3")
    for i in range(3):
        print(i, board[0+i*3], " ", board[1+i*3], " ", board[2+i*3])

def take_input(player):
    valid = False
    while not valid:
        player_answer = int(input("Ходит игрок " + player+" введите номер клетки, куда установите " + player ))
        if player_answer >= 1 and player_answer <= 9:
            if(str(board[player_answer-1]) not in "XO"):
                board[player_answer-1] = player
            valid = True
        else:
            print("Эта клетка уже занята!")

def check_win(board):
    win_position = ((0,1,2),(3,4,5),(6,7,8),(0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
    for each in win_position:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

def main(board):
    counter = 0
    wine = False
    while not wine:
        draw_board(board)
        if counter % 2 == 0:
            take_input("X")
            counter += 1
        else:
            take_input("0")
            counter += 1
        if counter > 4:
            tpm = check_win(board)
            if tpm:
                print(tpm, "Выйграл!")
                wine = True
                break
        if counter == 9:
            print("Ничья!")
            break
main(board)
draw_board(board)

