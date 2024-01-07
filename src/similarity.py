from math import sqrt

class Similarities:
    #%%
    def __init__(self, userToItem):
        self.userToItem = userToItem
        self.userSize = len(userToItem) - 1
        self.itemSize = len(userToItem[-1]) - 1
        self.average = [0.0] * (self.userSize + 1)
        self.itemToItem = []

    #%%
    def buildItemToItemC(self):
        self.itemToItem = [[0.0] * (self.itemSize + 1) for _ in range(self.itemSize + 1)]

        for i in range(1, self.itemSize + 1):
            for j in range(1, self.itemSize + 1):
                top, bleft, bright = 0, 0, 0
                cnt = 0

                for k in range(1, self.userSize + 1):
                    if self.userToItem[k][i] == 0 or self.userToItem[k][j] == 0:
                        continue

                    cnt += 1
                    top += self.userToItem[k][i] * self.userToItem[k][j]
                    bleft += self.userToItem[k][i] * self.userToItem[k][i]
                    bright += self.userToItem[k][j] * self.userToItem[k][j]

                if cnt < 1:
                    self.itemToItem[i][j] = 0
                else:
                    self.itemToItem[i][j] = top / (sqrt(bleft) * sqrt(bright))

    #%%
    def getAverage(self):
        for i in range(1, self.userSize + 1):
            cnt = 0
            for j in range(1, self.itemSize + 1):
                if self.userToItem[i][j] == 0:
                    continue
                cnt += 1
                self.average[i] += self.userToItem[i][j]
            self.average[i] /= cnt if cnt > 0 else 1

    #%%
    def buildItemToItemP(self):
        self.getAverage()
        self.itemToItem = [[0.0] * (self.itemSize + 1) for _ in range(self.itemSize + 1)]

        for i in range(1, self.itemSize + 1):
            for j in range(1, self.itemSize + 1):
                top, bleft, bright = 0, 0, 0
                cnt = 0

                for k in range(1, self.userSize + 1):
                    if self.userToItem[k][i] == 0 or self.userToItem[k][j] == 0:
                        continue

                    cnt += 1
                    top += (self.userToItem[k][i] - self.average[k]) * (self.userToItem[k][j] - self.average[k])
                    bleft += (self.userToItem[k][i] - self.average[k]) * (self.userToItem[k][j] - self.average[k])
                    bright += (self.userToItem[k][j] - self.average[k]) * (self.userToItem[k][j] - self.average[k])

                if cnt < 1:
                    self.itemToItem[i][j] = 0
                else:
                    self.itemToItem[i][j] = top / (sqrt(bleft) * sqrt(bright))

    #%%
    def predict(self, user, item):
        top, bottom = 0, 0

        # given untrained items
        if item > self.itemSize:
            return 3

        for i in range(1, self.itemSize + 1):
            if self.userToItem[user][i] == 0:
                continue
            bottom += abs(self.itemToItem[item][i])
            top += self.itemToItem[item][i] * self.userToItem[user][i]

        if bottom == 0:
            return 3

        rating = top / bottom
        return int(rating + 0.5)
