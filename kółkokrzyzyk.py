board = [1,2,3,4,5,6,7,8,9]
board_size = 3
def print_board():
    pass
    print('_' * 4 * board_size)
    for i in range(board_size):
        print((' '* 3 +'|')*3)
        print( '', board[i*3], '|' ,board[1 + i * 3], '|', board[2+i*3], '|')
        print(('_'* 3 +'|')*3)
def game_step():
    pass      

def check_win():
    pass
def start_game():
    current_player = 'X'
    step = 1
    print_board()
    while (step<10):
        index = input('pierwszy gracz ' + current_player +'.proszę wybrać numer kradki (0- wyjście):' )
        step+=1
        if (index== '0'):
            break
print('witamy w kółko i krzyzyk!')
start_game()