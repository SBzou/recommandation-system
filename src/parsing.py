import csv

#%%
def parse_context_to_csv(cxt_path, csv_path, lines_to_skip=338):
    with open(cxt_path, 'r') as file:
        for _ in range(lines_to_skip):
            next(file)

        context_data = [line.strip() for line in file]

        #Convert "X" in 1 and "." in 0
        binary_data = [list(map(lambda char: 1 if char == 'X' else 0, line)) for line in context_data]

    with open(csv_path, 'w', newline='') as csv_path:
        csv_writer = csv.writer(csv_path)
        csv_writer.writerows(binary_data)
