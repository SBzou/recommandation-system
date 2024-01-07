from math import sqrt
from typing import List

class UserToUser:
    def __init__(self, userToItem: List[List[int]]):
        self.userToItem = userToItem
        self.userSize = len(userToItem)
        self.itemSize = len(userToItem[0])

    def user_similarity(self, u, v):
        if u == v:
            return -1
        else:
            top, cu, cv = 0, 0, 0
            for j in range(self.itemSize):
                top += self.userToItem[u][j] * self.userToItem[v][j]
                cu += self.userToItem[u][j]
                cv += self.userToItem[v][j]

            if top > 0:
                return top / sqrt(cu * cv)
            return 0

    def build_user_similarities(self, u):
        user_similarities = [self.user_similarity(u, v) for v in range(self.userSize)]
        return user_similarities

    def select_neighbor(self, user_similarities, n):
        user_similarities_copy = user_similarities.copy()
        user_index = []
        for i in range(n):
            max_similarity = max(user_similarities_copy)
            neighbor = user_similarities_copy.index(max_similarity)
            user_similarities_copy[neighbor] = 0
            user_index.append(neighbor)
        return user_index

    def user_predict(self, u, i, n):
        user_similarities = self.build_user_similarities(u)
        user_index = self.select_neighbor(user_similarities, n)
        su, ci = 0, 0

        for j in range(self.itemSize):
            if self.userToItem[u][j] != 0:
                ci += 1

        sum_cv, sum_cj = 0, 0

        for index in user_index:
            v = index
            sum_cv += 1 / sqrt(self.get_user_number_rating(v))
            for j in range(self.itemSize):
                if self.userToItem[u][j] == 1 and self.userToItem[v][j] == 1:
                    sum_cj += 1 / sqrt(self.get_item_number_rating(j))

            su += self.userToItem[v][i] * sum_cv * sum_cj
            sum_cv, sum_cj = 0, 0

        if ci > 0:
            return su
        return -1

    def get_user_number_rating(self, u):
        #Return the number of ratings that user u has assigned, 1 if user has given no rating 
        return max(sum(self.userToItem[u]), 1)

    def get_item_number_rating(self, i):
        #Return the number of ratings that item i has assigned, 1 if item has given no rating
        return max(sum(row[i] for row in self.userToItem), 1)
