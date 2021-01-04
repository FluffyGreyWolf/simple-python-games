board_values = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',]
game_on = True
symbol = 'a'

def clear_screen():
    print('\n'*100)

def game_board():
    print(board_values[6] + '|' + board_values[7] + '|' + board_values[8])
    print(board_values[3] + '|' + board_values[4] + '|' + board_values[5])
    print(board_values[0] + '|' + board_values[1] + '|' + board_values[2])

def xo_decision():
    x = True
    global  symbol

    while x == True:
        symbol = input('You want to be X or O? ')
        if symbol == 'X' or symbol == 'O' or symbol == 'x' or symbol == 'o':
            x = False
        else:
            print('Wrong symbol!')
    return symbol


def choose_field():
    position = int(input('Choose position of your symbol (from 1-9 starting att the bottom left): '))
    global  symbol
    if board_values[position - 1] == ' ':
        for item in board_values:
            board_values[position - 1] =  symbol.capitalize()
            clear_screen()
            game_board()
            print(board_values)
    else:
        print('This position is already taken!')

    if symbol.capitalize() == 'X':
        symbol = 'O'
    else:
        symbol = 'X'


xo_decision()
while game_on:
    choose_field()


