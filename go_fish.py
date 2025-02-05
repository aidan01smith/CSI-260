import random

# card class is just defined by itself and the rank
class Card:
    def __init__(self, rank):
        self.rank = rank

# make the deck class which is pretty simple with help from random where we can shuffle the cards
class Deck:
    def __init__(self):
        self.cards = [Card(rank) for rank in range(1, 14) for _ in range(4)]
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop() if self.cards else None


# player class is also pretty simple as we are just building the empty lists and filling out the names of the players
class Player:
    def __init__(self, name):
        
        self.name = name
        
        self.hand = []
        
        self.books = []

    def ask_for_rank(self):

        # the new line makes it look nice :)
        print(f"\n{self.name}'s hand:", [card.rank for card in self.hand])
        
        rank = int(input(f"{self.name}, enter a rank to ask for: "))

        # I got a bit of help from an LLM with this if statement as it was giving me a lot of trouble
        if rank not in {card.rank for card in self.hand}:
            print("You must ask for a rank in your hand!")
            
            return self.ask_for_rank()
        
        return rank

    # function to give the cards to the player when they go fish
    def give_cards(self, rank):
        cards = [card for card in self.hand if card.rank == rank]
        
        self.hand = [card for card in self.hand if card.rank != rank]
        
        return cards

    # simply appending to the list when the player picks up a card
    def receive_card(self, card):
        if card:
            self.hand.append(card)
            self.check_for_books()

    #checking to see if the books are completed with the 4 of a kind in each hand (some help was given by LLM)
    def check_for_books(self):
        for rank in set(card.rank for card in self.hand):
            if sum(1 for card in self.hand if card.rank == rank) == 4:
                
                self.books.append(rank)
                
                self.hand = [card for card in self.hand if card.rank != rank]
                
                print(f"{self.name} completed a book of {rank}s!")

# now we get into the game rules - these were kind of hard to map out logically for each player
class GoFish:
    def __init__(self):
        self.deck = Deck()
        self.players = [Player(input("Enter name for Player 1: ")), Player(input("Enter name for Player 2: "))]
        
        # i thought it made more sense to just leave the for variable blank because i didn't know what i would have put in there
        for _ in range(5):
            for player in self.players:
                
                player.receive_card(self.deck.draw())
                
        # set the count = 0 which indicates that player 1 need to go first
        self.current_player = 0

    
    def play_turn(self):
        
        player = self.players[self.current_player]
        
        opponent = self.players[1 - self.current_player]
        
        # makes sure that the player has enough cards their hand using the not boolean expression
        if not player.hand:
            print(f"{player.name} has no cards and skips the turn.")
            return

        rank = player.ask_for_rank()
        
        if any(card.rank == rank for card in opponent.hand):
            print(f"{opponent.name} gives all {rank}s.")
            for card in opponent.give_cards(rank):
                player.receive_card(card)
        else:
            print(f"{opponent.name} says 'Go Fish!'")
            player.receive_card(self.deck.draw())

        # oh how the turns have tabled
        self.current_player = 1 - self.current_player

    # check to see if cards are in hand and if they are not then game ends
    def is_game_over(self):
        return all(not player.hand for player in self.players) and not self.deck.cards

    # got some help with an LLM on this becuase I was struggling to find a place to put the game start
    def play(self):
        print("\nStarting Go Fish!")
        while not self.is_game_over():
            self.play_turn()
            for player in self.players:
                print(f"{player.name}: {len(player.hand)} cards, Books: {player.books}")

        print("\nGame Over!")
        # I figured out that max finds the highest value and that others used lambda with a single expression to make the code just a little shorter (I think it is pretty cool cuz I never used it before)
        winner = max(self.players, key=lambda p: len(p.books))
        print(f"The winner is {winner.name} with {len(winner.books)} books!")

# to start the game/run the script directly. I found some other documentation that started their game like this
if __name__ == "__main__":
    GoFish().play()
