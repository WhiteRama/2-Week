import DeckClass
import GamerClass
import time
import os

deck = DeckClass.Deck()

p1 = GamerClass.Player()
dealer = GamerClass.Dealer()

####GAME FUNCTION####

def weightJudge(gamer):
    
    gamer.weight = 0
    gamer.weightList = []
    gamer.countWeight()

    if (gamer.weight == 21) and (len(gamer.hand) == 2):
        print(gamer.name + " GOT BLACK JACK!!!")
        print(gamer.name + " WIN")
        os.system("pause")
        exit()
        

    if gamer.weight > 21:
        print(gamer.name + " GOT BUSTED")
        print(gamer.name + " LOSE")
        os.system("pause")
        exit()

def finalJudge():

    if p1.weight > dealer.weight:
        print(p1.name + " WIN")


    elif p1.weight == dealer.weight:
        print("DRAW")

    else:
        print(dealer.name + " WIN")

    os.system("pause")
    exit()

def printGamerWeight():
   
    print(p1.name + " : " + str(p1.weight))
    print(dealer.name + " : " + str(dealer.weight))

def startGame():            # new game start
    os.system("cls")

    deck.reset()

    ## First Hit ##

    p1.drawCard(deck.draw())
    print(p1.name + "'s hand : ")
    print(p1.hand)
    time.sleep(0.8)

    dealer.drawCard(deck.draw())
    print(dealer.name + "'s hand : ")
    print(dealer.hand)

    time.sleep(1.3)

    ## Second Hit ###

    os.system("cls")

    p1.drawCard(deck.draw())
    print(p1.name + "'s hand : ")
    print(p1.hand)
    weightJudge(p1)

    time.sleep(0.8)

    dealer.drawCard(deck.draw())
    print(dealer.name + "'s hand : ")
    print(dealer.hand)
    weightJudge(dealer)

    time.sleep(1.3)

    printGamerWeight()

def playerHit():

    if p1.hit:
        p1.askHit()

    if p1.hit:
        p1.drawCard(deck.draw())

    os.system("cls")

    print(p1.name + "'s hand : ")
    print(p1.hand)
    time.sleep(0.8)

def dealerHit():

    if dealer.hit:
        dealer.dealerHitRule()

    if dealer.hit:
        dealer.drawCard(deck.draw())

    print(dealer.name + "'s hand : ")
    print(dealer.hand)


#### GAME ####

startGame()

while p1.hit or dealer.hit:

    playerHit()
    weightJudge(p1)

    dealerHit()
    weightJudge(dealer)

    printGamerWeight()

    if (not dealer.hit) and (p1.weight > dealer.weight):
        break

finalJudge()