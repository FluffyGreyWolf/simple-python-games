# Created along with course
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

game_on = True

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += ('\n' + card.__str__())
        return deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1

class Coins:

    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

def take_bet(coins):

    while True:
        try:
            coins.bet = int(input('How many coins would you like to bet? '))
        except:
            print('Thats not a number!')
        else:
            if coins.bet > coins.total:
                print('Not enought coins!', coins.total)
            else:
                break

def hit(deck, hand):

    single_card = deck.deal()
    hand.add_card((single_card))
    hand.adjust_for_ace()

def hit_or_stand(deck, hand):
    global  game_on

    while True:
        print('What you want to do?')
        print('1 - Hit')
        print('2 - Stand')
        x = input()

        if x == '1':
            hit(deck, hand)

        elif x == '2':
            game_on = False

        else:
            print('Wrong number!')
            continue
        break



def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n ')

def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)

def player_bust(player, dealer, coins):
    print('Bust player!')
    coins.lose_bet()

def player_wins(player, dealer, coins):
    print('Player wins!')
    coins.win_bet()

def dealer_bust(player, dealer, coins):
    print('Player wins! Dealer busted!')
    coins.win_bet()

def dealer_wins(player, dealer, coins):
    print('Dealer wins!')
    coins.lose_bet()

def push(player, dealer):
    print(('Tie! Push!'))

while True:

    print('Welcome to blackjack!')

    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    player_coins = Coins()

    take_bet(player_coins)

    show_some(player_hand, dealer_hand)

    while game_on:

        hit_or_stand(deck, player_hand)

        if player_hand.value > 21:
            player_bust(player_hand, dealer_hand, player_coins)
            break

    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

            show_all(player_hand, dealer_hand)

            if dealer_hand.value > 21:
                dealer_bust(player_hand, dealer_hand, player_coins)
            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand, dealer_hand, player_coins)
            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand, dealer_hand, player_coins)
            else:
                push(player_hand, dealer_hand)

    print(f'Player total coins = {player_coins.total}')

    new_game = input('Do you want to play again? y/n ')

    if new_game[0].lower() == 'y':
        game_on = True
        continue
    else:
        print('Thank you for playing!')
