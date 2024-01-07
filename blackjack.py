import random
color = ["heart","diamonds","spades","clubs"]
jack=10
queen=10
king=10
ace=11
values = [2,3,4,5,6,7,8,9,10,jack,queen,king,ace]
cards = []

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
num_player = 2
num_cards = 2
for i in range(num_player):
    inner = []
    players.append(inner)

for i in range(num_cards):
    for j in range(num_player):
        players[j].append(cards.pop(0))

#Printing decks
print(players[0])
print(players[1])
print("\n")

#Counting values of cards
def count(values):
    sum = 0
    pom = 0
    for i in range(len(values)):
        pom = values[i]
        sum = sum + pom
        i = i + 1
        if(values.count(11) >= 1 and sum > 21):
            sum = sum - 10
    return(sum)

#Main game func
def blackjack(tab1, tab2, cards):
    free_val, free_col = map(list, zip(*cards))
    values1, color1 = map(list, zip(*tab1))
    values2, color2 = map(list, zip(*tab2))
    print("karty gracza 1 to : ")
    print(values1)
    print("karty gracza 2 to : ")
    print(values2)

    win = False   
    while (win != True):
        sum1= count(values1)
        sum2= count(values2)
        print("suma wartosci gracza 1 to : ")
        print(sum1)
        print("suma wartosci gracza 2 to : ")
        print(sum2)
        print("\n")
        if(sum1 == 21 and sum2 == 21):
            print("Remis, obaj gracze wygrali")
            break
        if(sum1 > 21 and sum2 > 21):
            print("Remis, obaj gracze przegrali")
            break
        if(sum1 <= 21 and sum2 > 21):
            print("Gracz 1 wygral gre")
            break
        if(sum2 <= 21 and sum1 > 21):
            print("Gracz 2 wygral gre")
            break
        if(sum1 == 21 and sum2 < 21):
            print("Gracz 1 wygral gre")
            break
        if(sum2 == 21 and sum1 < 21):
            print("Gracz 2 wygral gre")
            break
        if(sum1 < 21):
            values1.append(free_val.pop(0))
            print("karty gracza 1 to : ")
            print(values1)
        if(sum2 < 21):
            values2.append(free_val.pop(0))
            print("karty gracza 2 to : ")
            print(values2)

#Starting game
blackjack(players[0], players[1], cards)