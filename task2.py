import json
import csv


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME) as csv_file:
        csv_data = csv.reader(csv_file)
        headers = next(csv_data)
        data=[]
        for row in csv_data:
            row_dict={}
            for i in range(len(headers)):
                row_dict[headers[i]] = row[i]
            data.append(row_dict)

    with open(OUTPUT_FILENAME, 'w') as json_file:
        json.dump(data, json_file, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
