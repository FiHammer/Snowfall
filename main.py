import printer
import time
import random
import math


def beginSnow():
    snowflakes = random.randint(startFlakeRnd[0], startFlakeRnd[1])
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
    num = random.randint(0, 100)
    if num > 42:
        beginSnow()


def fallDown():
    global maxHeigh

    for botIndexNum in range(lp.maxX):
        # beginnt vom Boden

        curHi = lp.maxY - 1
        curEl = lp.lineConts[curHi][botIndexNum]

        haveAbove = lp.lineConts[curHi - 1][botIndexNum] == snowFlake
        # jetztige maxHeigh

        while curHi > maxHeigh or haveAbove:  # haveAbove für stehen beleiben ÜBER maxH
            haveAbove = lp.lineConts[curHi - 1][botIndexNum] == snowFlake
            if haveAbove and curEl != snowFlake:
                # snowflake fällt!
                lp.lineConts[curHi][botIndexNum] = snowFlake
                lp.lineConts[curHi - 1][botIndexNum] = empty

            curHi -= 1
            curEl = lp.lineConts[curHi][botIndexNum]
            if curHi == 0:
                break
            try:
                haveAbove = lp.lineConts[curHi - 1][botIndexNum] == snowFlake
            except IndexError:
                print(curHi, botIndexNum)

        if curHi < maxHeigh:
            maxHeigh = curHi

    # alles über maxH
    oldLC = lp.lineConts.copy()
    lp.lineConts[0] = lp.emptyLC[0].copy()
    for lineNum in range(maxHeigh):
        if lineNum + 1 == maxHeigh:
            break
        lp.lineConts[lineNum + 1] = oldLC[lineNum].copy()


if "__main__" == __name__:
    runningBase = True
    while runningBase:
        resetByLine = 3

        # generation of enviroment

        maxX = 236
        maxY = 63

        waitTime = random.randint(50, 100) / 100  # waittime between 0,5s - 1s
        snowFRnd = random.randint(0, 10)  # snowFlake type
        if snowFRnd == 0:
            snowFlake = "*"
        else:
            snowFlake = "X"
        emptyRnd = random.randint(0, 25)  # empty type
        if snowFRnd == 0 and snowFRnd != 0:
            empty = "*"
        elif snowFRnd == 1:
            empty = "-"
        elif snowFRnd == 2:
            empty = "."
        elif snowFRnd == 3:
            empty = ":"
        elif snowFRnd == 4:
            empty = "|"
        else:
            empty = " "

        startFlakeRnd = (round((math.pow(waitTime, -1)) * 4), round((maxX / 11) * waitTime))

        lp = printer.LinePrinter(empty=empty, full=snowFlake)
        lp.fillLC()

        maxHeigh = lp.maxY

        running = True
        beginSnow()
        while running:
            lp.printLC()
            dropSnow()

            if lp.lineConts[resetByLine] == lp.fullLC[1]:
                running = False

            time.sleep(waitTime)
        lp.lineConts = lp.emptyLC.copy()
