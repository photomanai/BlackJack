import random
import os

os.system("cls")

symbols = ["♦ ", "♠ ", "♥ ", "♣ "]
symbol_index = 0

nums = ["A ", "2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 ", "9 ", "10", "J ", "Q ", "K "]
num_index = 0

deck = []
deck_len = 0
deck_index = 0

croupier_hand = []
croupier_card = []
croupier_score = 0

player_hand = []
player_card = []
player_score = 0

money = 1000
bet = 0
player_win = None


def resetGame():

    global croupier_card, croupier_hand, croupier_score, player_card, player_hand, player_score, bet

    croupier_hand = []
    croupier_card = []
    croupier_score = 0

    player_hand = []
    player_card = []
    player_score = 0

    bet = 0

    reset_deck()


def start_game():
    global croupier_card, croupier_hand, croupier_score, player_card, player_hand, player_score, bet, money

    if money <= 0:
        loseGame()
    else:

        os.system("cls")
        print("Your Money: ", money)

        while True:
            try:
                bet = int(input("Enter your bet: "))
                if bet > money:
                    print("You entered too much money")
                    input()
                    os.system("cls")
                    print("Your Money: ", money)
                else:
                    break
            except ValueError:
                print("Invalid number! Please enter an integer.")
                input()
                os.system("cls")
                print("Your Money: ", money)

        print(" ")
        print("Your bet: ", bet)
        print(" ")
        print("Croupier Card")
        croupier_call_card()
        croupier_card, croupier_hand = deal_card(1)
        croupier_score = score_macine(croupier_card)
        print("Croupier Score:", croupier_score)

        print(" ")

        print("Player Card")
        player_card, player_hand = deal_card(2)
        player_score = score_macine(player_card)
        print("Player Card:", player_score)

        print(" ")

        if player_score == 21:
            check_game(croupier_score, player_score)
            checkMoney()
            start_game()
        else:
            restume_game()


def restume_game():
    global croupier_card, croupier_hand, croupier_score, player_card, player_hand, player_score

    while True:
        chose = input("Enter Your Chose(Hit/Stand): ")

        if chose in ["Hit", "hit", "H", "h"]:
            player_card, player_hand = add_card(player_card, player_hand)
            player_score = score_macine(player_card)
            if player_score > 21:
                check_game(croupier_score, player_score)
                player_stand()
                break
            player_hit()

        if chose in ["Stand", "stand", "S", "s"]:
            croupier_call_card()
            player_stand()
            break

    checkMoney()
    input("Press enter to continue the game. ")
    resetGame()
    start_game()


def reset_deck():
    for i in nums:
        for k in symbols:
            deck.append(i + k)


def deal_card(count):
    game_card = []
    game_hand = []
    for i in range(count):
        deck_len = len(deck)
        deck_index = random.randint(0, deck_len - 1)
        game_card.append(deck[deck_index][0] + deck[deck_index][1])
        card = f"""
    ┌─────────┐
    │{deck[deck_index][0] + deck[deck_index][1]}       │
    │         │
    │         │
    │    {deck[deck_index][2]}    │
    │         │
    │         │
    │       {deck[deck_index][0] + deck[deck_index][1]}│
    └─────────┘"""
        game_hand.append(card)
        del deck[deck_index]

    cards = {}
    for i in range(count):
        k = f"card{i+1}"
        cards[k] = game_hand[i].split("\n")

    mix_hand = []
    mix_card = ""

    for i in range(len(cards["card1"])):
        mix_card = ""
        for j in range(count):
            k = f"card{j+1}"
            mix_card += cards[k][i]
        mix_hand.append(mix_card)
    mix_hand = "\n".join(mix_hand)

    print(mix_hand)

    return game_card, game_hand


def add_card(game_card, game_hand):

    deck_len = len(deck)
    deck_index = random.randint(0, deck_len - 1)
    game_card.append(deck[deck_index][0] + deck[deck_index][1])
    card = f"""
    ┌─────────┐
    │{deck[deck_index][0] + deck[deck_index][1]}       │
    │         │
    │         │
    │    {deck[deck_index][2]}    │
    │         │
    │         │
    │       {deck[deck_index][0] + deck[deck_index][1]}│
    └─────────┘"""
    game_hand.append(card)
    del deck[deck_index]

    cards = {}
    for i in range(len(game_hand)):
        k = f"card{i+1}"
        cards[k] = game_hand[i].split("\n")

    mix_hand = []
    mix_card = ""

    for i in range(len(cards["card1"])):
        mix_card = ""
        for j in range(len(game_hand)):
            k = f"card{j+1}"
            mix_card += cards[k][i]
        mix_hand.append(mix_card)
    mix_hand = "\n".join(mix_hand)

    # print(mix_hand)

    return game_card, game_hand


def call_card(game_hand):

    count = len(game_hand)

    cards = {}
    for i in range(count):
        k = f"card{i+1}"
        cards[k] = game_hand[i].split("\n")

    mix_hand = []
    mix_card = ""

    for i in range(len(cards["card1"])):
        mix_card = ""
        for j in range(count):
            k = f"card{j+1}"
            mix_card += cards[k][i]
        mix_hand.append(mix_card)
    mix_hand = "\n".join(mix_hand)

    print(mix_hand)


def score_macine(game_card):
    game_score = 0

    for i in game_card:
        if i in ["J ", "Q ", "K "]:
            game_score += 10
        elif i in ["A "]:
            game_score += 11
        else:
            game_score += int(i)

    return game_score


def check_game(croupier_score, player_score):
    global player_win
    if player_score == 21 and croupier_score != 21:
        print("BLACKJACK , Player Win")
        player_win = True
    elif croupier_score == 21 and player_score != 21:
        print("BLACKJACK , Player Lose")
        player_win = False
    elif player_score > 21:
        print("Player Lose")
        player_win = False
    elif croupier_score > 21 or player_score > croupier_score:
        print("Player Win")
        player_win = True
    elif croupier_score > player_score:
        print("Player Lose")
        player_win = False
    elif player_score > croupier_score:
        print("Player Win")
        player_win = True
    else:
        print("Push")
        player_win = None


def croupier_call_card():
    global croupier_card, croupier_hand, croupier_score, player_card, player_hand, player_score
    if croupier_score < 17:
        croupier_card, croupier_hand = add_card(croupier_card, croupier_hand)
        croupier_score = score_macine(croupier_card)
        # print(croupier_score)
        croupier_call_card()


def player_hit():
    global croupier_card, croupier_hand, croupier_score, player_card, player_hand, player_score, bet

    os.system("cls")

    print(" ")
    print("Your bet: ", bet)
    print(" ")
    print("Croupier Card")
    call_card(croupier_hand)
    print("Croupier Score:", croupier_score)

    print(" ")

    print("Player Card")
    call_card(player_hand)
    print("Player Card:", player_score)

    print(" ")


def player_stand():
    global croupier_card, croupier_hand, croupier_score, player_card, player_hand, player_score, player_win

    os.system("cls")

    print(" ")
    print("Your bet: ", bet)
    print(" ")
    print("Croupier Card")
    call_card(croupier_hand)
    print("Croupier Score:", croupier_score)

    print(" ")

    print("Player Card")
    call_card(player_hand)
    print("Player Card:", player_score)

    print(" ")
    check_game(croupier_score, player_score)


def checkMoney():
    global player_win, money, bet
    if player_win == True:
        money = money + bet
    elif player_win == False:
        money = money - bet


def loseGame():
    os.system("cls")
    print(
        """
  __     __           _                    
  \ \   / /          | |                   
   \ \_/ /__  _   _  | |     ___  ___  ___ 
    \   / _ \| | | | | |    / _ \/ __|/ _ |
     | | (_) | |_| | | |___| (_) \__ \  __/
     |_|\___/ \__,_| |______\___/|___/\___|
                                           
                                           
"""
    )
    input()


print(
    """
  __          __  _                             
  \ \        / / | |                            
   \ \  /\  / /__| | ___ ___  _ __ ___   ___    
    \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \   
     \  /\  /  __/ | (_| (_) | | | | | |  __/   
  ____\/_ \/ \___|_|\___\___/|_| |_| |_|\___|   
 |  _ \| |          | |      | |          | |   
 | |_) | | __ _  ___| | __   | | __ _  ___| | __
 |  _ <| |/ _` |/ __| |/ /   | |/ _` |/ __| |/ /
 | |_) | | (_| | (__|   < |__| | (_| | (__|   < 
 |____/|_|\__,_|\___|_|\_\____/ \__,_|\___|_|\_|
           _____                                
          / ____|                               
         | |  __  __ _ _ __ ___   ___           
         | | |_ |/ _` | '_ ` _ \ / _ \          
         | |__| | (_| | | | | | |  __/          
          \_____|\__,_|_| |_| |_|\___|          
                                                
             
"""
)

input("Press enter to continue the game: ")

reset_deck()
start_game()
