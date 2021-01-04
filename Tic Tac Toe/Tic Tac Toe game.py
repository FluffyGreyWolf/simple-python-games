board_values = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
game_on = True
play_again_true_false = True
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
    print(f'Now is {symbol.capitalize()} turn!')
    return symbol


def choose_field():
    global  symbol
    user_input = input('Choose position of your symbol (from 1-9 starting at the bottom left): ')
    if user_input.isdigit():
        position = int(user_input)
        if position in range(1, 10):
            if board_values[position - 1] == ' ':
                for item in board_values:
                    board_values[position - 1] =  symbol.capitalize()
                    clear_screen()
                    game_board()
            else:
                print('This position is already taken!')

            if symbol.capitalize() == 'X':
                symbol = 'O'
            else:
                symbol = 'X'

            print(f'Now is {symbol.capitalize()} turn!')
        else:
            print('Wrong number!')
    else:
        print('Thats not a digit!')

def win_check_x():
    global  game_on
    if (board_values[0] == 'X' and board_values[1] == 'X' and board_values[2] == 'X') or (board_values[3] == 'X' and board_values[4] == 'X' and board_values [5] == 'X') or (board_values[6] == 'X' and board_values[7] == 'X' and board_values[8] == 'X') or (board_values[0] == 'X' and board_values[3] == 'X' and board_values[6] == 'X') or (board_values[1] == 'X' and board_values[4] == 'X' and board_values[7] == 'X') or (board_values[2] == 'X' and board_values[5] == 'X' and board_values[8] == 'X'):
        print('\nX WON!')
        game_on = False
        return game_on
    elif (board_values[0] == 'O' and board_values[1] == 'O' and board_values[2] == 'O') or (board_values[3] == 'O' and board_values[4] == 'O' and board_values [5] == 'O') or (board_values[6] == 'O' and board_values[7] == 'O' and board_values[8] == 'O') or (board_values[0] == 'O' and board_values[3] == 'O' and board_values[6] == 'O') or (board_values[1] == 'O' and board_values[4] == 'O' and board_values[7] == 'O') or (board_values[2] == 'O' and board_values[5] == 'O' and board_values[8] == 'O'):
        print('\nO WON!')
        game_on = False
        return game_on
    else:
        pass

def tie_check():
    global game_on
    x = 0
    if ' ' in board_values:
        x += 1
    else:
        pass
    if x == 0:
        clear_screen()
        game_board()
        print('GAME OVER - TIE')
        game_on = False
        return game_on
    else:
        pass

def play_again():
    global play_again_true_false
    global game_on
    global board_values
    global symbol
    if game_on == False:
        play_again_anwser = input('Do you want to play again? yes/no: ')
        if play_again_anwser == 'y' or play_again_anwser == 'yes'or play_again_anwser == 'Yes' or play_again_anwser == 'YES':
            game_on = True
            board_values = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
            symbol = 'a'
            game()
        elif play_again_anwser == 'n' or play_again_anwser == 'no' or play_again_anwser == 'No' or play_again_anwser == 'NO':
            play_again_true_false = False
            return play_again_true_false
        else:
            print('Wrong anwser!')
            play_again()

def game():
    xo_decision()
    while game_on:
        choose_field()
        win_check_x()
        tie_check()
    while play_again_true_false:
        play_again()

game()