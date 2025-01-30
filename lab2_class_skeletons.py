class player():
    '''
    The player class that defines which player is who and what cards they have
    The player might also be replaced with a bot that plays the game itself
    '''

    def __init__(self, name, cards):
        self.name = name
        self.cards = cards

    def display(self):
        pass

    def draw(self):
        pass

    def play(self):
        pass

    def gofish(self):
        pass

    def check(self):
        pass    

    def __str__(self):
        return f"{self.name} has {self.cards}"
    
class deck():
    # the deck class that defines the deck of cards
    def __init__(self, cards):
        self.cards = cards

    def display(self):
        print(f"{self.cards}")

    def shuffle(self):
        pass

class card():

    # this is the card class to that defines the cards in the deck
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value}{self.suit}"
    
    def __eq__(self, other):    
        return self.value == other.value


# create a game class
# create the books list in a game class

class Game:
    def __init__(self, players, books, deck):
        self.players = players
        self.books = books
        self.deck = deck
        self.hands = {player: [] for player in players}
        self.deal()

    def deal(self):
        pass

    def print_hands(self):
        pass

    def winner(self):
        pass
    
