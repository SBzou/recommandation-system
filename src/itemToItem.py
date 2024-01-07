from math import sqrt
from typing import List

class ItemToItem:
    #%%
    def __init__(self, userToItem: List[List[int]]):
        self.userToItem = userToItem
        self.userSize = len(userToItem)
        self.itemSize = len(userToItem[0])
        self.itemToItem = [[0] * self.itemSize for _ in range(self.itemSize)]

    #%%
    def item_similarity(self, i, j):
        if i == j:
            return -1
        else:
            top, ci, cj = 0, 0, 0
            for u in range(self.userSize):
                top += self.userToItem[u][i] * self.userToItem[u][j]
                ci += self.userToItem[u][i]
                cj += self.userToItem[u][j]

            if top > 0:
                return top / sqrt(ci * cj)
            return 0

    #%%
    def build_item_similarities(self, i):
        item_similarities = [self.item_similarity(i, j) for j in range(self.itemSize)]
        return item_similarities

    #%%
    def select_neighbor(self, item_similarities, n):
        item_similarities_copy = item_similarities.copy()
        item_index = []
        for _ in range(n):
            max_similarity = max(item_similarities_copy)
            neighbor = item_similarities_copy.index(max_similarity)
            item_similarities_copy[neighbor] = 0
            item_index.append(neighbor)
        return item_index

    #%%
    def item_predict(self, u, i, n):
        item_similarities = self.build_item_similarities(i)
        item_index = self.select_neighbor(item_similarities, n)
        si, ci = 0, 0

        for j in range(self.itemSize):
            if self.userToItem[u][j] != 0:
                ci += 1

        sum_cj, sum_cv = 0, 0

        for index in item_index:
            j = index
            sum_cj += 1 / sqrt(self.get_item_number_rating(j))
            for v in range(self.userSize):
                if self.userToItem[v][i] == 1 and self.userToItem[v][j] == 1:
                    sum_cv += 1 / sqrt(self.get_user_number_rating(v))

            si += self.userToItem[u][j] * sum_cv * sum_cj
            sum_cv, sum_cj = 0, 0

        if ci > 0:
            return si
        return -1

    #%%
    def get_user_number_rating(self, u):
        #Return the number of ratings that user u has assigned, 1 if user has given no rating
        return max(sum(self.userToItem[u]), 1)
    #%%
    def get_item_number_rating(self, i):
        #Return the number of ratings that item i has assigned, 1 if item has given no rating
        return max(sum(row[i] for row in self.userToItem), 1)
