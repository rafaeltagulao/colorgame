import random
import csv

revenueArray = []

trials=10000

for trial in range(trials):

    rounds = 100
    numPart = 20
    revenue = 0

    #########################################

    #Generating money

    currMoney = []

    for x in range(numPart):
        currMoney.append(1000)

    #Generating random bet amount

    for round in range(rounds):

        betMoneyPart = []
        bills = [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 50, 50, 50, 50, 50, 100, 100]

        for randomBets in range(numPart):
            randBillOrder = random.randint(1,16)
            betMoneyPart.append(bills[randBillOrder])
        
    #########################################

        #Generating random bet color

        colors = ["yellow", "white", "pink", "blue", "red", "green"]

        betColorPart = []

        for numParts in range(numPart):
            randomColor = random.randint(0,5)
            betColorPart.append(colors[randomColor])

        #########################################
            
        #Generating random chosen 3 colors    
            
        chosenColor = []    

        for randomColors in range(3):
            randomColor = random.randint(0,5)
            chosenColor.append(colors[randomColor])
            
        #########################################
            
        #Generating how much each player wins
          
        boolResult = [None] * 5 
          
        for x in range(3):
            for y in range(5):
                if betColorPart[y] == chosenColor[x]:
                    currMoney[y] = currMoney[y] + betMoneyPart[y]
                    boolResult[y] = "win"
                    revenue = revenue - betMoneyPart[y]
                    
        for x in range(5):
            if boolResult[x] == None:
                currMoney[x] = currMoney[x] - betMoneyPart[x]
                revenue = revenue + betMoneyPart[x]
                
        revenueArray.append(revenue)

        #print(betMoneyPart)
        #print(betColorPart)
        #print(chosenColor)
        #print(boolResult)
        #print(currMoney)
        #print("")
        
    #print(currMoney)

print(revenueArray)

with open('colorgame20p100r.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for x in range(trials):
            writer.writerow([revenueArray[x]])


