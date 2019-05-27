import printer
import time
import random

empty = " "

lp = printer.LinePrinter(empty=empty)
lp.fillLC()

snowFlake = "X"
maxHeigh = lp.maxY


def beginSnow(minFalkes=3, maxFlakes=6):
    snowflakes = random.randint(minFalkes, maxFlakes)
    used = []
    for x in range(snowflakes):
        index = random.randint(0, lp.maxX - 1)
        while index in used:
            index = random.randint(0, lp.maxX - 1)
        used.append(index)
        lp.lineConts[0][index] = snowFlake


def moveDown(LC):
    oldLC = LC.copy()
    LC[0] = lp.emptyLC[0].copy()
    for lineNum in range(len(oldLC)):
        if lineNum + 1 == len(oldLC):
            break
        LC[lineNum + 1] = oldLC[lineNum].copy()
    return LC


def dropSnow():
    fallDown()
    num = random.randint(0, 2)
    if num == 1:
        if num == 2:
            beginSnow(maxFlakes=random.randint(2, 10))
        else:
            beginSnow()


def fallDown():
    global maxHeigh

    for botIndexNum in range(lp.maxX):
        # beginnt vom Boden

        curHi = lp.maxY - 1
        curEl = lp.lineConts[curHi][botIndexNum]

        haveAbove = lp.lineConts[curHi-1][botIndexNum] == snowFlake
        # jetztige maxHeigh

        while curHi > maxHeigh or haveAbove:  # haveAbove für stehen beleiben ÜBER maxH
            haveAbove = lp.lineConts[curHi-1][botIndexNum] == snowFlake
            if haveAbove and curEl != snowFlake:
                # snowflake fällt!
                lp.lineConts[curHi][botIndexNum] = snowFlake
                lp.lineConts[curHi - 1][botIndexNum] = empty

            curHi -= 1
            curEl = lp.lineConts[curHi][botIndexNum]
            haveAbove = lp.lineConts[curHi-1][botIndexNum] == snowFlake

        if curHi < maxHeigh:
            maxHeigh = curHi

    # alles über maxH
    oldLC = lp.lineConts.copy()
    lp.lineConts[0] = lp.emptyLC[0].copy()
    for lineNum in range(maxHeigh):
        if lineNum + 1 == maxHeigh:
            break
        lp.lineConts[lineNum + 1] = oldLC[lineNum].copy()





running = True
beginSnow()
while running:
    lp.printLC()
    dropSnow()
    #time.sleep(0.75)

