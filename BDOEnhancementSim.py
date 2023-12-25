import random

def test_run(baseProp, propRateChange):
    n = 0
    success = False
    while success == False:
        n += 1
        prop = baseProp+(propRateChange*(n-1))
        success = random.choices([True, False], weights=[prop, (1-prop)], k=1)[0]
    return n


if __name__ == "__main__":
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