import csv
from typing import List

class Input:
    #%%
    def __init__(self, filename: str):
        self.fin = open(filename)
        if not self.fin:
            print(f"{filename} file could not be opened")
            exit(0)

        self.parse_csv(filename)
        
    #%%
    def parse_csv(self, input_csv):
        with open(input_csv, 'r') as file:
            csv_reader = csv.reader(file)
            # Assuming the CSV file contains binary data (0 or 1)
            self.in_data = [list(map(int, line)) for line in csv_reader]

        # Assuming user_to_item is a matrix of the same size as the CSV data
        self.user_to_item = self.in_data.copy()

    #%%
    def get_input(self):
        return self.in_data

    #%%
    def get_user_to_item(self):
        return self.user_to_item
