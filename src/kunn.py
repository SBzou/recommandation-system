from math import sqrt
from typing import List
from src.userToUser import UserToUser
from src.itemToItem import ItemToItem

class Kunn:
    #%%
    def __init__(self, user_to_item: List[List[int]], neighbor: int):
        self.user_to_item = user_to_item
        self.user_to_user = UserToUser(user_to_item)
        self.item_to_item = ItemToItem(user_to_item)
        self.neighbor = neighbor

    #%%
    def prediction(self, u, i):
        prediction_user = self.user_to_user.user_predict(u, i, self.neighbor)
        prediction_item = self.item_to_item.item_predict(u, i, self.neighbor)
        cu = self.user_to_user.get_user_number_rating(u)
        ci = self.user_to_user.get_item_number_rating(i)
        return (prediction_user + prediction_item) / (sqrt(cu * ci))

    #%%
    def get_mat_binary(self):
        pred_mat = [[0] * len(self.user_to_item[0]) for _ in range(len(self.user_to_item))]
        for i in range(len(self.user_to_item)):
            for j in range(len(self.user_to_item[0])):
                pred = self.prediction(i, j)

                if pred < 1:
                    pred = 0
                else:
                    pred = 1

                pred_mat[i][j] = pred
        return pred_mat
