import random

class Card:
    def __init__(self, rank):
        self.rank = rank

class Deck:
    def __init__(self):
        self.cards = [Card(rank) for rank in range(1, 14) for _ in range(4)]
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop() if self.cards else None

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.books = []

    def ask_for_rank(self):
        print(f"\n{self.name}'s hand:", [card.rank for card in self.hand])
        rank = int(input(f"{self.name}, enter a rank to ask for: "))
        if rank not in {card.rank for card in self.hand}:
            print("You must ask for a rank in your hand!")
            return self.ask_for_rank()
        return rank

    def give_cards(self, rank):
        cards = [card for card in self.hand if card.rank == rank]
        self.hand = [card for card in self.hand if card.rank != rank]
        return cards

    def receive_card(self, card):
        if card:
            self.hand.append(card)
            self.check_for_books()

    def check_for_books(self):
        for rank in set(card.rank for card in self.hand):
            if sum(1 for card in self.hand if card.rank == rank) == 4:
                self.books.append(rank)
                self.hand = [card for card in self.hand if card.rank != rank]
                print(f"{self.name} completed a book of {rank}s!")

class GoFish:
    def __init__(self):
        self.deck = Deck()
        self.players = [Player(input("Enter name for Player 1: ")), Player(input("Enter name for Player 2: "))]
        for _ in range(5):
            for player in self.players:
                player.receive_card(self.deck.draw())
        self.current_player = 0

    def play_turn(self):
        player = self.players[self.current_player]
        opponent = self.players[1 - self.current_player]

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

        self.current_player = 1 - self.current_player

    def is_game_over(self):
        return all(not player.hand for player in self.players) and not self.deck.cards

    def play(self):
        print("\nStarting Go Fish!")
        while not self.is_game_over():
            self.play_turn()
            for player in self.players:
                print(f"{player.name}: {len(player.hand)} cards, Books: {player.books}")

        print("\nGame Over!")
        winner = max(self.players, key=lambda p: len(p.books))
        print(f"The winner is {winner.name} with {len(winner.books)} books!")

if __name__ == "__main__":
    GoFish().play()
