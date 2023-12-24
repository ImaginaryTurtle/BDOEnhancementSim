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
    baseProp = float(input("Base propabiblity:"))
    propRateChange = float(input("Rate of change per fail:"))
    numRuns = int(input("Number of runs:"))

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
    print(f"Average Number of Runs: {totNumber/numRuns}")
    print(f"Max Runs: {maxRuns}")
    print(f"Bins: {dict(sorted(bins.items()))}")
    print(f"All Runs: {allRuns}")