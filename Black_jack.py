import random
suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4,'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    def __str__(self):
        return f'{self.rank} of {self.suit}'

class Deck:
    def __init__(self):
        self.cards = []
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))
    def shuffle(self):
        random.shuffle(self.cards)
    def deal(self):
        return self.cards.pop()

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    def addcard(self, card):
        self.cards.append(card)
        self.value += card.value
        if card.rank == 'Ace':
            self.aces += 1
        self.adjust_for_ace()
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
class Chips:
    def __init__(self):
        self.total = 0
        self.bet = 0

    def deposit(self, total):
        self.total += total
    def take_bet(self,bet):
        self.bet=bet
        self.total -= self.bet

    def blackjack_bet(self):
        self.total += self.bet * 2.5
    def win_bet(self):
        self.total += self.bet * 2
    def draw_bet(self):
        self.total += self.bet


class Player(Hand,Chips):
    def __init__(self, name):
        Hand.__init__(self)
        Chips.__init__(self)
        self.name = name
        self.isblackjack = False
    def play_hand(self,deck):
        self.isblackjack = False
        second_hand = None
        while True:
            bet_to_take = input("How many chips would you like to bet (min 25 and must be n*25)?")
            if bet_to_take.isdigit() and int(bet_to_take) >= 25 and int(bet_to_take)%25 ==0 and int(bet_to_take) <= self.total:
                break
            else:
                print("Invalid input, try again.")
                continue
        self.take_bet(int(bet_to_take))
        self.addcard(card_(deck))
        print(self.cards[-1])
        self.addcard(card_(deck))
        print(self.cards[-1])
        print(self.value)
        if self.can_split():
            option = input("Would you like to split the hand? (y/n)")
            if option == 'y':
                second_hand = self.split(deck)
                print("You choose to split the hand.")
                self.total-=self.bet
            else:
                print("You choose not to split.")

        print(f"Playing first hand ({[str(c) for c in self.cards]}):")
        self.play_individual_split_hand(deck)
        if second_hand:
            print("Now playing second hand")
            self.play_individual_split_hand(deck.second_hand)

        if self.value == 21:
            print(f'{self.name} BlackJack!')
            self.isblackjack = True
        return second_hand

    def can_split(self):
        return len(self.cards)==2 and self.cards[0].rank == self.cards[1].rank and self.total >= self.bet

    def split(self,deck):
        second_hand = Hand()
        second_hand.addcard(self.cards.pop())
        self.value = self.cards[0].value

        self.addcard(card_(deck))
        second_hand.addcard(card_(deck))
        print(f"First hand: {[str(c) for c in self.cards]} (value={self.value})")
        print(f"Second hand: {[str(c) for c in second_hand.cards]} (value={second_hand.value})")

        return second_hand

    def play_individual_split_hand(self,deck,hand=None):
        if hand is None:
            hand = self
        while hand.value < 21:
            print(f"Current value {hand.value}")
            option = input("Would you like to take the card? (y/n)")
            if option == 'y':
                self.addcard(card_(deck))
                print(self.cards[-1])
                print(self.value)
            elif option == 'n':
                break
            else:
                print("Invalid input, try again.")



class Dealer(Player):
    def __init__(self):
        Player.__init__(self, 'Dealer')

    def play_deal(self,deck, playervalue):
        self.isblackjack = False
        self.addcard(card_(deck))
        print(self.cards[-1])
        self.addcard(card_(deck))
        print(self.cards[-1])
        print(self.value)
        if self.value == 21:
            print('Dealer have BlackJack!')
            self.isblackjack = True
        while self.value < 17:
            self.addcard(card_(deck))
            print(self.cards[-1])
            print(self.value)

        while self.value < 21 and self.value < playervalue < 21:
            self.addcard(card_(deck))
            print(self.cards[-1])
            print(self.value)

def card_(shuffled_deck):
    card_to_play = shuffled_deck.deal()
    return card_to_play

name = input("Write down player name: ")
player1 = Player(name)
dealer1 = Dealer()
while True:
    amount_to_deposit=input("How many chips would you like to buy?: ")
    if amount_to_deposit.isdigit():
        break
    else:
        print("Invalid input, try again.")
        continue
player1.deposit(int(amount_to_deposit))
while True:
    print(f'player {player1.name} total is: {player1.total}')
    if player1.total ==0:
        print('You have no chips left.')
        break
    player1.cards=[]
    player1.value =0
    player1.aces =0
    player1.isblackjack = False
    dealer1.cards=[]
    dealer1.value = 0
    dealer1.aces = 0
    dealer1.is_blackjack = False
    deck = Deck()
    deck.shuffle()
    second_hand = player1.play_hand(deck)
    # 1️⃣ Sprawdź, czy gracz przekroczył 21
    if player1.value > 21:
        print(f'{player1.name} busts (over 21)! Dealer wins.')

    else:
        # 2️⃣ Krupier gra dopóki ma mniej niż 17 (typowe zasady)
        dealer1.play_deal(deck,player1.value)

        # 3️⃣ Sprawdź wyniki blackjacka
        if player1.isblackjack and dealer1.isblackjack:
            print("DRAW (both have Blackjack!)")
            player1.draw_bet()
        elif player1.isblackjack:
            print(f"{player1.name} wins with BLACKJACK!")
            player1.blackjack_bet()
        elif dealer1.isblackjack:
            print("Dealer wins with BLACKJACK!")

        # 4️⃣ Sprawdź, kto przekroczył 21
        elif dealer1.value > 21:
            print(f"Dealer busts! {player1.name} wins!")
            player1.win_bet()
        # 5️⃣ Porównanie wartości
        elif player1.value > dealer1.value:
            print(f"{player1.name} wins with {player1.value} vs dealer's {dealer1.value}!")
            player1.win_bet()
        elif player1.value < dealer1.value:
            print(f"Dealer wins with {dealer1.value} vs {player1.name}'s {player1.value}.")

        else:
            print("DRAW (same value).")
            player1.draw_bet()

        if second_hand:
            print("\n--- Checking second hand ---")
            if second_hand.value > 21:
                print(f"{player1.name} busts on second hand!")
            else:
                dealer1.play_deal(deck, second_hand.value)
                if dealer1.value > 21 or second_hand.value > dealer1.value:
                    print(f"{player1.name} wins on second hand!")
                    player1.win_bet()
                elif second_hand.value < dealer1.value:
                    print("Dealer wins on second hand.")
                else:
                    print("Second hand draw.")
                    player1.draw_bet()
    # 🔁 zapytanie o kontynuację
    x = input("Do you want to continue? (y/n): ").lower()
    if x == 'y':
        continue
    elif x == 'n':
        break
    else:
        print("Invalid input, try again.")
