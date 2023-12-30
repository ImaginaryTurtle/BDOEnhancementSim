import random

def test_run(baseProp, propRateChange):
    n = 0
    success = False
    while success == False:
        n += 1
        prop = baseProp+(propRateChange*(n-1))
        success = random.choices([True, False], weights=[prop, (1-prop)], k=1)[0]
    return n

def mythic_horse():
    baseProp = float(input("Base propabiblity: "))
    propRateChange = float(input("Rate of change per fail: "))
    numRuns = int(input("Number of runs: "))
    numTaps = int(input("Number of taps: "))

    totNumber = 0
    maxRuns = 0
    bins = {}
    allRuns = []
    for n in range(numRuns):
        run = test_run(baseProp, propRateChange)
        maxRuns = max([maxRuns, run])
        totNumber += run
        if run in bins.keys():
            bins[run] += 1
        else:
            bins[run] = 1
        allRuns.append(run)
    averageRuns = totNumber/numRuns
    print(f"Average Number of Runs: {averageRuns}")
    print(f"Max Runs: {maxRuns}")
    #print(f"Bins: {dict(sorted(bins.items()))}")
    #print(f"All Runs: {allRuns}")
    atOrLower = 0
    above = 0
    for x in allRuns:
        if x <= numTaps:
            atOrLower += 1
        else:
            above += 1
    print(f"Lower: {atOrLower}")
    print(f"Higher: {above}")

def accessory_tap(successRate, downgradeChance):
    success = random.choices([True, False], weights=[successRate, (1-successRate)], k=1)[0]

    if not success:
        downgrade = random.choices([True, False], weights=[downgradeChance, (1-downgradeChance)], k=1)[0]
        if downgrade:
            return "downgrade"
        else:
            return "fail"
    else:
        return "success"

def accessory():
    #Debo Earring:
    #cronNumber = [95,288,865,2405,11548]
    #cronCost = 1.642
    #accessoryValues = [825,2470,7400,20600,99000,300000]

    #Disto:
    cronNumber = [62,187,562,1562,7499]
    cronCost = 1.642
    accessoryValues = [342,870,2700,8000,25300,165000]
    
    #Stacks =  number : chance
    #   Pri =  22 : .72, 58 : .90
    #   Duo =  42 : .504, 80 : .58
    #   Tri =  44 : .405, 110 : .504
    #   Tet =  110 : .30, 130 : .31
    #   Pen =  255 : .1325, 275 : .1425

    successRates = [.72,.504,.405,.30,.1325]
    downgradeChance = 0.4

    for n in range(len(successRates)):
        
        resultDict = {"success" : 0,
                        "fail" : 0,
                        "downgrade" : 0}
        noCronDict = {"success" : 0,
                      "fail" : 0}

        for x in range(100000):
            result = accessory_tap(successRates[n], downgradeChance)
            if result == "success":
                resultDict[result] += (accessoryValues[n+1] - (accessoryValues[n] + accessoryValues[0] + (cronCost * cronNumber[n])))
                noCronDict[result] += (accessoryValues[n+1] - (accessoryValues[n] + accessoryValues[0]))
            elif result == "fail":
                resultDict[result] += (-1*(accessoryValues[0] + (cronCost * cronNumber[n])))
                noCronDict[result] += (-1*(accessoryValues[n] + accessoryValues[0]))
            else:
                resultDict[result] += (accessoryValues[max(n-1,0)] - (accessoryValues[n] + accessoryValues[0] + (cronCost * cronNumber[n])))
                noCronDict["fail"] += (-1*(accessoryValues[n] + accessoryValues[0]))

        for i in resultDict.keys():
            resultDict[i] = resultDict[i]/100000

        for i in noCronDict.keys():
            noCronDict[i] = noCronDict[i]/100000

        cronProfits = sum(resultDict.values())
        noCronProfits = sum(noCronDict.values())
        print(f"{n} Result: \
        \n    Profits with crons    = {cronProfits} \
        \n    Profits without crons = {noCronProfits}")

def accessory_count():
    #Stacks =  number : chance
    #   Pri =  22 : .72, 58 : .90
    #   Duo =  42 : .504, 80 : .58
    #   Tri =  44 : .405, 110 : .504
    #   Tet =  110 : .30, 130 : .31
    #   Pen =  255 : .1325, 275 : .1425

    successRates = [.9,.58,.504,.31,.1425]
    downgradeChance = 0.4

    averageTaps = []

    numRuns = 100000

    for s in range(len(successRates)):
        accessoryCounter = 0
        for x in range(numRuns):
            result = ""
            if len(averageTaps) > 0:
                accessoryCounter += averageTaps[s-1]
            else:
                accessoryCounter += 1
            while result != "success":
                result = accessory_tap(successRates[s], downgradeChance)
                accessoryCounter += 1
                if result == "downgrade":
                    if len(averageTaps) == 1:
                        accessoryCounter += (averageTaps[s-1] - 1)
                    if len(averageTaps) > 1:
                        accessoryCounter += (averageTaps[s-1] - averageTaps[s-2])
        averageTaps.append(accessoryCounter/numRuns)
        print(f"average accessories for {s}: {averageTaps[s]}       *Success Rate: {successRates[s]}")

    print(f"Accessory Counts: {averageTaps}")


def boss_gear():
    return 0

if __name__ == "__main__":
    print("Select Type: \
    \n1. T9 & T10 Horse \
    \n2. Accessories \
    \n3. Accessory Count \
    \n4. Boss Gear")

    while True:
        userSelection = input("Input: ")
        if userSelection == "1":
            mythic_horse()
            break
        elif userSelection == "2":
            accessory()
            break
        elif userSelection == "3":
            accessory_count()
            break
        elif userSelection == "4":
            boss_gear()
            break
        else:
            print("Invalid Selection \
            \nExample: '1' for T9 or T10 Horse Enhancement")
