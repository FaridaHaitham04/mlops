import csv

def read_csv_as_rows(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        
        headers = next(reader)
        print(f"Headers: {headers}\n")
        
        for row in reader:
            print(row)


read_csv_as_rows('sample-simple.csv')