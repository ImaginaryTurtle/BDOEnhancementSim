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
    cronNumber = [62,187,562,1562,7499]
    cronCost = 1.642
    successRates = [.72,.53,.4215,.3025,.1325]
    downgradeChance = 0.4

    for n in range(len(successRates)):
        resultDict = {"success" : 0,
                        "fail" : 0,
                        "downgrade" : 0}
        for x in range(100000):
            result = accessory_tap(successRates[n], downgradeChance)
            resultDict[result] += 1
        print(f"{n} Result: {resultDict}")


def boss_gear():
    return 0

if __name__ == "__main__":
    print("Select Type: \
    \n1. T9 & T10 Horse \
    \n2. Accessories \
    \n3. Boss Gear")

    while True:
        userSelection = input("Input: ")
        if userSelection == "1":
            mythic_horse()
            break
        elif userSelection == "2":
            accessory()
            break
        elif userSelection == "3":
            boss_gear()
            break
        else:
            print("Invalid Selection \
            \nExample: '1' for T9 or T10 Horse Enhancement")
