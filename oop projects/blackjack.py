import random


class Card:
    def __init__(self,value,suit):
        self.value=value
        self.suit=suit

    def show(self):
        print(f'{self.value} of {self.suit}')

class Deck:
    def __init__(self):
        self.card=[]
        self.build()

    def build(self):
        for s in ['Hearts','Diamonds','Clubs','Spades']:
            for v in range(1,13):
                self.card.append(Card(v,s))

    def showCard(self):
        for c in self.card:
            c.show()

     #fisher-yates
    def shuffle(self):
        for i in range(len(self.card)-1,0,-1):
            r=random.randint(0,i)
            self.card[i],self.card[r]=self.card[r],self.card[i]

    def draw(self):
        return self.card.pop()

class Player:
    def __init__(self,name):
        self.name=name
        self.hand=[]

    def drawCard(self,deck):
        self.hand.append(deck.draw())
        return self

    def showHand(self):
        for card in self.hand:
            card.show()

    def discard(self):
        self.hand.pop()


deck=Deck()
deck.build()
deck.shuffle()


alex=Player('Alex')
alex.drawCard(deck).drawCard(deck)
alex.discard()
alex.showHand()






