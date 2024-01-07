import random
color = ["heart","diamonds","spades","clubs"]
jack=11
queen=12
king=13
ace=14
values = [2,3,4,5,6,7,8,9,10,jack,queen,king,ace]
cards = []
i=0
j=0
#Creating deck
for i in range(4):
    for j in range (13):
        a = color[i]
        b = values[j]
        cards.append([b, a]) 
#Shuffling deck
def shuffle(x):
    random.shuffle(x)
shuffle(cards)

#Creating player's decks
players = []
num_player = 4
num_cards = 5
for i in range(num_player):
    inner = []
    players.append(inner)

for i in range(num_cards):
    for j in range(num_player):
        players[j].append(cards.pop(0))
#Printing decks
print(players[0])
print(players[1])

#Main game func
def battle(tab1, tab2):
    while(tab1 != 0 or tab2 != 0):
        if(len(tab1) == 0):
            print("Gracz 2 wygral GRE")
            break
        if(len(tab2) == 0):
            print("Gracz 1 wygral GRE")
            break
        x=tab1.pop(0)
        y=tab2.pop(0)
        print(x)
        print(y)
        if(x>y):
            tab1.append(x)
            tab1.append(y)
            print("Gracz 1 wygral bitwe")
            print(players[0])
            print(players[1])
        elif(y>x):
            tab2.append(y)
            tab2.append(x)
            print("Gracz 2 wygral bitwe")
            print(players[0])
            print(players[1])
        else:
            tab1.append(x)
            tab2.append(y)
            print("Remis")
            print(players[0])
            print(players[1])

#Starting game
battle(players[0], players[1])