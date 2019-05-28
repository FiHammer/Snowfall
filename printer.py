import os
import copy

class LinePrinter:
    def __init__(self, maxX=236, maxY=63, empty=" ", full="X", star="*", stars=None):
        if stars is None:
            stars = []
        self.stars = stars
        self.maxX = maxX
        self.maxY = maxY

        self.allCont = empty
        self.fullCont = full
        self.lineConts = []
        self.emptyLC = []
        self.fullLC = []
        self.stars = []
        self.star = star

    def fillLC(self):
        # Filling the line Conts
        for lineNum in range(self.maxY):
            self.lineConts.append([])
            for indexNum in range(self.maxX):
                self.lineConts[lineNum].append(self.allCont)

        for lineNum in range(self.maxY):
            self.emptyLC.append([])
            for indexNum in range(self.maxX):
                self.emptyLC[lineNum].append(self.allCont)

        for lineNum in range(self.maxY):
            self.fullLC.append([])
            for indexNum in range(self.maxX):
                self.fullLC[lineNum].append(self.fullCont)

    def printLC(self, lc):
        # PRINT IT
        lc = copy.deepcopy(self.lineConts)
        for star in self.stars:
            if lc[star[0]][star[1]] == self.allCont:
                lc[star[0]][star[1]] = self.star

        os.system("cls")
        for line in lc:
            fullLine = ""
            for index in line:
                fullLine += index
            print(fullLine)
