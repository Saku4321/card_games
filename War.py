import random
suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4,'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}
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

class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []
    def remove_one(self):
        if not self.all_cards:
            return None
        return self.all_cards.pop()
    def add_card(self, new_cards):
        #for multiple card objects
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        #for single card object
        else:
            self.all_cards.append(new_cards)
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'

#GAME SETUP
if __name__ == "__main__":
    p1_name= input('Player 1 name: ')
    player_one=Player(p1_name)
    p2_name= input('Player 2 name: ')
    player_two=Player(p2_name)
    deck = Deck()
    deck.shuffle()
    for i in range((len(deck.cards) // 2)):
        player_one.add_card(deck.deal())
        player_two.add_card(deck.deal())
    def movement(player_one, player_two):
        move = []
        move.append(player_one.remove_one())
        move.append(player_two.remove_one())

        print(f'\n{player_one.name} plays: {move[-2]}')
        print(f'{player_two.name} plays: {move[-1]}')

        while True:
            # porównanie kart
            if move[-2].value > move[-1].value:
                print(f'\n{player_one.name} wins the round!\n')
                player_one.add_card(move)
                break
            elif move[-2].value < move[-1].value:
                print(f'\n{player_two.name} wins the round!\n')
                player_two.add_card(move)
                break
            else:
                print("\n🔥 WAR! 🔥\n")

                # sprawdzenie kart
                if len(player_one.all_cards) < 4:
                    print(f"{player_one.name} doesn't have enough cards! {player_two.name} wins the game!")
                    return 2
                elif len(player_two.all_cards) < 4:
                    print(f"{player_two.name} doesn't have enough cards! {player_one.name} wins the game!")
                    return 1

                print("Each player places 3 cards face down and 1 face up...\n")

                # 3 zakryte + 1 odkryta od każdego
                for i in range(4):
                    move.append(player_one.remove_one())
                    move.append(player_two.remove_one())

                # pokazujemy ostatnie odkryte karty
                print(f'{player_one.name} reveals: {move[-2]}')
                print(f'{player_two.name} reveals: {move[-1]}')

        return 0  # gra trwa dalej
    def check_if_end(player_one, player_two):
        if len(player_one.all_cards) ==0:
            return 1
        elif len(player_two.all_cards) ==0:
            return 2
        else:
            return -1
    round_num = 0
    while True:
        round_num += 1
        print(f'--- ROUND {round_num} ---')
        result = movement(player_one, player_two)
        if result == 1 or check_if_end(player_one, player_two) == 1:
            print(f'\n{player_one.name} WINS THE GAME!')
            break
        elif result == 2 or check_if_end(player_one, player_two) == 2:
            print(f'\n{player_two.name} WINS THE GAME!')
            break
        input("Press ENTER to continue to the next round...")