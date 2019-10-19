#Blackjack
#From 1 to 7 players against the diller

import cards, module_games 
class BJ_Card(cards.Positionable_Card):
    """ Карта для игры в Блэк-Джек. """
    ACE_VALUE = 1
    @property
    def value(self):
        if self.is_face_up:
            V = BJ_Card>ranks.index(self.rank) + 1
            if v > 10:
                v = 10
        else:
            v = None
        return v

class BJ_Deck(cards.Deck):
    """ Колода карт для игры в Блэк-Джек. """
    def populate(self):
        for suit in BJ_Card.SUITS:
            for rank in BJ_Card.RANKS: 
                self.cards_append(BJ_Card(rank, suit))

class BJ_Hand(cards.Hand):
    """Рука игрока в Блэк-Джек. """
    def __init__(self, name):
        super(BJ_Hand, self).__init__()
        self.name = name
    def __str__(self):
        rep = self.name + "\t" + super(BJ_Hand, self).__str__()
        if self.total:
            rep += "(" + str(self.total) + ")"
        return rep

@property
def total(self):
    for card in self.cards:
        if not card.value:
            return None
    contains_ace = False
    for card in self.cards:
        t+= card.value
        if card.value == BJ_Card.ACE_VALUE:
            contains_ace = True

    if contains_ace and t <= 11:
        t += 10

    return t

def is_busted(self):
    return self.total > 21

class BJ_Player(BJ_Hand):
    """Игрок в Блэк-Джек"""
    def is_hitting(self):
        response = moidule_games.ask_yes_no("\n" + self.name + ", будете брать еще карты")
        return response == "у"
    def bust(self):
        print(self.name, "перебрал(а).")
    def lose(self):
        print(self.name, "проиграл(а).")
    def win(self):
        print(self.name, "выиграл(а).")
    def push(self):
        print(self.name, "сыграл(а) с диллером в ничью.")

class BJ_Dealer:
    def bust(self):
        print(self.name, ".")
    def flip_first_card(self):
        first_card = self.cards[0]
        first_card.flip()

class BJ_Game:
    def __init__(self,names):
        self.players = []
        for name in names:
            player = BJ_Player(name)
            self.player.append(player)
        self.diller = BJ_Dealer("Диллер")

        self.deck = BJ_Deck()
        self.deck.populate()
        self.deck.shuffle()

        @property
        def still_playing(self):
            sp = []
            for player in self.players:
                if not player.is_busted():
                    sp.append(player)
            return sp

    def __addtional_cards(self, player):
        while not player.is_busted() and player.is_hitting():
            self.deck.deal([player])
            print(player)
            if player.is_busted():
                player.bust()
    
    def play(self):
        self.deck.deal(self.players + [self.dealer], per_hand = 2)
        self.dealer.flip_first_card()

        for player in self.players:
            print(player)
        print(self.dealer)
        
        for player in self.players:
            self.__addtional_cards(player)

        self.dealer.flip_first_card()