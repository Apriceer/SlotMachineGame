print("""
░██████╗██╗░░░░░░█████╗░████████╗░██████╗
██╔════╝██║░░░░░██╔══██╗╚══██╔══╝██╔════╝
╚█████╗░██║░░░░░██║░░██║░░░██║░░░╚█████╗░
░╚═══██╗██║░░░░░██║░░██║░░░██║░░░░╚═══██╗
██████╔╝███████╗╚█████╔╝░░░██║░░░██████╔╝
╚═════╝░╚══════╝░╚════╝░░░░╚═╝░░░╚═════╝░
""")

import random

money = 100
bet = 10
slotLength = 3

commands = ["help","spin","bet","money"]
slotIcons = ["❤️","🎉","7️⃣","🍒","👾"]

def rollNums():
    randTable = []
    symbols = []
    index = 0
    for x in range(slotLength):
        rand = random.randrange(0,len(slotIcons))
        randTable.insert(index,rand)
        symbols.insert(index,slotIcons[rand])
        index += 1
    return [randTable,symbols]
    
def spinSlot(money):
    if money >= bet:
        money -= bet
        print(f"-{bet}")
        spinNumbers = rollNums()
        # 0 is the numbers 1 is the symbols
        print(spinNumbers[1])
                
        ammountPer = []
                
        for x in range(len(slotIcons)):
                    
            ammountPer.insert(x-1,0)
            for y in spinNumbers[0]:
                if x == y:
                    ammountPer[x-1] += 1
                    
            if ammountPer[x-1] > 1 and not x == 2:
                money += bet*(2**(ammountPer[x-1]-1))
                print(f"+{bet*(2**(ammountPer[x-1]-1))}")
                        
            if ammountPer[x-1] > 0 and x == 2:
                money += bet*(2**(ammountPer[x-1]))
                print(f"+{bet*(2**(ammountPer[x-1]))}")
                            
                #print(ammountPer)
                
                
        print(f"Money: {money}")
        
    else:
        print("Insuficient money, get a loan or lower your bet")

while True:
    print("Input command")
    command = input()
    print()
    if command in commands:
        if command == "help":
            print("List of Commands:")
            for x in commands:
                print(x)
                
        if command == "spin":
            
                spinSlot(money)
            
        """
            if money >= bet:
                money -= bet
                print(f"-{bet}")
                spinNumbers = rollNums()
                # 0 is the numbers 1 is the symbols
                print(spinNumbers[1])
                
                ammountPer = []
                
                for x in range(len(slotIcons)):
                    
                    ammountPer.insert(x-1,0)
                    for y in spinNumbers[0]:
                        if x == y:
                            ammountPer[x-1] += 1
                    
                    if ammountPer[x-1] > 1 and not x == 2:
                        money += bet*(2**(ammountPer[x-1]-1))
                        print(f"+{bet*(2**(ammountPer[x-1]-1))}")
                        
                    if ammountPer[x-1] > 0 and x == 2:
                        money += bet*(2**(ammountPer[x-1]))
                        print(f"+{bet*(2**(ammountPer[x-1]))}")
                            
                #print(ammountPer)
                
                
                print(f"Money: {money}")
            else:
                print("Insuficient money, get a loan or lower your bet")
        """
            
        if command == "bet":
            print("Insert bet")
            try:
                betInput = int(input())
                bet = betInput
            except:
                print("Invalid bet")
        if command == "money":
            print(money)
    else:
        print("Invalid command")
        print()
    
    print()