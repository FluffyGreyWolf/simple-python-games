import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

class Card:

    def __init__(self, suits, ranks):

        self.suits = suits
        self.ranks = ranks
        self.values = values[ranks]

    def __str__(self):
        return self.ranks + ' of ' + self.suits

class Deck:

    def __init__(self):

        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

class Player:

    def __init__(self, name):
        self.name = name
        self.all_player_cards = []

    def add_card(self, new_card):
        self.all_player_cards.append(new_card)

player_human = Player('Player')
player_bot = Player('Bot')

new_deck = Deck()
new_deck.shuffle()

game_on = True
bot_cards_value = 0
player_cards_value = 0

player_human.add_card(new_deck.deal_one())
player_human.add_card(new_deck.deal_one())
player_bot.add_card(new_deck.deal_one())
player_bot.add_card(new_deck.deal_one())


def bot_cards():

    print('\nBot cards: ')
    value = 0

    for i in player_bot.all_player_cards[:-1]:
        print(i)
        value += i.values
    print('And one card is hidden!')
    print(f'Of value: {value} (without hidden card!)\n')

def player_cards():

    print('\nYour cards: ')
    value = 0

    for i in player_human.all_player_cards:
        print(i)
        value += i.values

    print(f'Of value: {value}\n')

ace = False

def counting_values():

    global bot_cards_value
    global player_cards_value

    player_cards_value = 0
    bot_cards_value = 0

    for i in player_bot.all_player_cards:
        bot_cards_value += i.values

    for i in player_human.all_player_cards:
        player_cards_value += i.values
    if ace == True:
        player_cards_value -= 10

x = 0
decision_on = True

def decision():
    global x
    global decision_on
    print('\nWhay you want to do: ')
    print('1 - hit (take one more card)')
    print('2 - stay (computer makes a move)')

    while True:
        x = input('Choose number: ')

        if x == '1' or x == '2':
            if x == '2':
                decision_on = False
                return x
            else:
                return x
        else:
            print('Wrong number!')
def game():
    print('\n')
    bot_cards()
    player_cards()
    counting_values()

while game_on:

    game()
    decision()

    while decision_on:
        if x == '1':
            if new_deck.all_cards[-1].values == 11:
                print('Choose card value: ')
                print('1 - 1 point')
                print('2 - 11 points')
                y = input()
                if y == '1':
                    player_human.add_card(new_deck.deal_one())
                    player_cards_value -= 10
                    ace = True
                    game()
                else:
                    print('Wrong number!')
            else:
                player_human.add_card(new_deck.deal_one())
                game()
            if player_cards_value > 21:
                print(f'Values of bot cards: {bot_cards_value}')
                print(f'Values of player cards: {player_cards_value}\n')
                print('Game over! You have over 21 points! Bot wins!')
                game_on = False
                break
            else:
                decision()
        else:
            decision_on = False
            break

    while not decision_on:

        if bot_cards_value == 21 and player_cards_value != 21:
            print(f'Values of bot cards: {bot_cards_value}')
            print(f'Values of player cards: {player_cards_value}\n')
            print('Game over! Bot have 21 points! Bot wins!')
            break
        elif bot_cards_value == 21 and player_cards_value == 21:
            print(f'Values of bot cards: {bot_cards_value}')
            print(f'Values of player cards: {player_cards_value}\n')
            print('Game over! You bot have 21 points! Tie!')
            break
        elif bot_cards_value < 21 and bot_cards_value > player_cards_value:
            print(f'Values of bot cards: {bot_cards_value}')
            print(f'Values of player cards: {player_cards_value}\n')
            print('Game over! Bot have more points than you! Bot wins!')
            break
        elif bot_cards_value > 21:
            print(f'Values of bot cards: {bot_cards_value}')
            print(f'Values of player cards: {player_cards_value}\n')
            print('Game over! Bot have over 21 points! You win!')
            break
        elif bot_cards_value < 21 and bot_cards_value < player_cards_value:
            player_bot.add_card(new_deck.deal_one())
            bot_cards()
            counting_values()
            continue
    break