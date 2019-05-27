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


def getStars():
    stars = []
    for x in range(starQuan):
        stars.append((random.randint(0, starEnd-1), random.randint(0, maxX-1)))
    return stars


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
        emptyRnd = random.randint(0, 25)  # empty type
        starRnd = random.randint(0, 35)  # star type
        if starRnd == 0 and snowFRnd != 0:
            star = " "
        elif starRnd == 1:
            star = "O"
        elif starRnd == 2:
            star = "'"
        elif starRnd == 3:
            star = '"'
        elif starRnd == 4:
            star = "~"
        elif starRnd == 5 and emptyRnd != 2:
            star = "."
        elif starRnd == 6:
            star = ","
        else:
            star = "*"
        if snowFRnd == 0 and star != "*":
            snowFlake = "*"
        else:
            snowFlake = "X"
        if emptyRnd == 0 and snowFRnd != 0 and star != "*":
            empty = "*"
        elif emptyRnd == 1:
            empty = "-"
        elif emptyRnd == 2:
            empty = "."
        elif emptyRnd == 3:
            empty = ":"
        elif emptyRnd == 4:
            empty = "|"
        else:
            empty = " "

        starEnd = random.randint(round(maxY / 7), round(maxY / 2))
        val1 = round((maxX * maxY) / 2500)
        val2 = round(maxX * maxY * starEnd / 20000)
        while val2 < val1:
            val2 += 2
        starQuan = random.randint(val1, val2)

        startFlakeRnd = (round((math.pow(waitTime, -1)) * 4), round((maxX / 11) * waitTime))

        lp = printer.LinePrinter(empty=empty, full=snowFlake, star=star)
        lp.fillLC()
        lp.stars = getStars()

        maxHeigh = lp.maxY

        running = True
        beginSnow()
        while running:
            lp.printLC(lp.lineConts.copy())
            dropSnow()
            
            i = 0
            for index in lp.lineConts[resetByLine]:
                if index == snowFlake:
                    i += 1
            
            if i/maxX > 0.6:
                running = False

            time.sleep(waitTime)
        lp.lineConts = lp.emptyLC.copy()
