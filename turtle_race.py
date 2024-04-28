from turtle import Turtle
from random import randint

laura = Turtle()
rick = Turtle()
lauren= Turtle()
joe = Turtle()

laura.color('red')
laura.shape('turtle')
laura.penup()
laura.goto(-160,100)
laura.pendown()

rick.color('blue')
rick.shape('turtle')
rick.penup()
rick.goto(-160,70)
rick.pendown()

coins = 100
lw = randint(1,2)
rw = randint(1,2)


while coins > 0: 
    ods = lw/rw
    print("\n")
    print(f"Lauren/Rick ods are {ods}")
    bet = int(input(f"Place a bet, coins left {coins} "))
    who = input("Place a bet on Lauren or Rick ")
    
    coins = coins - bet
    
    if who == "Lauren":
        bet_lauren = bet
    if who == "Rick":
        bet_rick = bet
        
    list_lf = []
    list_rf =[]
    
    for movememnt in range(100):
        lf = randint(1,5)
        rf = randint(1,5)
        laura.forward(lf)
        rick.forward(rf)
        list_lf.append(lf)
        list_rf.append(rf)
        
    list_lf = sum(list_lf)
    list_rf = sum(list_rf)

    if list_lf>list_rf:
        lw+=1
        print("Laura won")
        print(f"Laura {lf}")
        print(f"Rick {rf}")
        if who == "Lauren":
            coins = coins + bet*ods      
    else:
        rw+=1
        print("Rick won")
        print(f"Laura {lf}")
        print(f"Rick {rf}")
        if who == "Rick":
            coins = coins + bet/ods  
    
    if input("Next race Y: ") == "Y":
        laura.goto(-160,100)
        rick.goto(-160,70)
            
        
        
input("Press Enter to close")