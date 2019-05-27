import os


class LinePrinter:
    def __init__(self, maxX=236, maxY=63, empty=" ", full = "X"):
        self.maxX = maxX
        self.maxY = maxY

        self.allCont = empty
        self.fullCont = full
        self.lineConts = []
        self.emptyLC = []
        self.fullLC = []

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


    def printLC(self):
        # PRINT IT
        os.system("cls")
        for line in self.lineConts:
            fullLine = ""
            for index in line:
                fullLine += index
            print(fullLine)
