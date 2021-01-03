board_values = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',]

def clear_screen():
    print('\n'*100)

def game_board():
    print(board_values[6] + '|' + board_values[7] + '|' + board_values[8])
    print(board_values[3] + '|' + board_values[4] + '|' + board_values[5])
    print(board_values[0] + '|' + board_values[1] + '|' + board_values[2])


def xo_decision():
    x = True

    while x == True:
        symbol = input('You want to be X or O? ')
        if symbol == 'X' or symbol == 'O' or symbol == 'x' or symbol == 'o':
            x = False
        else:
            print('Wrong symbol!')
    return symbol.capitalize()

symbol = xo_decision()

def choose_field():
    position = int(input('Choose position of your symbol (from 1-9 starting att the bottom left): '))

    if board_values[position] == ' ':
        for item in board_values:
            board_values[position - 1] = symbol

    else:
        print('This position is already taken!')

    game_board()

choose_field()
