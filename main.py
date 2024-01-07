import csv
from src.parsing import parse_context_to_csv
from src.input import Input
from src.kunn import Kunn

import time as time

if __name__ == "__main__":
    start = time.time()
    #%%
    print("\nCSV data generation")
    cxt_path = "data/context.cxt"
    csv_path = "data/context.csv"
    parse_context_to_csv(cxt_path, csv_path)
    print("\nCSV data generated successfully")

    #%%
    print("\nuserToItem creation")
    base_input_reader = Input(csv_path)
    user_to_item = base_input_reader.get_user_to_item()
    print("\nuserToItem is ready")

    #%%
    print("\nBeginning of Kunn process")
    kunn = Kunn(user_to_item, len(user_to_item[0]))
    pred_mat = kunn.get_mat_binary()
    print("\nEnd of Kunn Process")

    #%%
    print("\nWriting predictions into prediction.csv")
    predicion_path = "data/prediction.csv"
    with open(predicion_path, "w", newline="") as out:
        csv_writer = csv.writer(out)
        for row in pred_mat:
            csv_writer.writerow(row)

    print("\prediction.csv is ready")

    #%%
    print("\nQuality Check ")
    quality = 0.0
    for i in range(len(pred_mat)):
        for j in range(len(pred_mat[0])):
            quality += abs(pred_mat[i][j] - user_to_item[i][j])
    quality /= len(pred_mat) * len(pred_mat[0])
    quality = 1 - quality

    print(f"\nThe quality is: {quality * 100:.2f}%")

    print(time.time() - start)
