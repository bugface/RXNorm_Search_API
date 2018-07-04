import pandas as pd
from functools import partial
import csv
import json


def check_int(row, col_name):
    if row[col_name].isdigit():
        return 1
    else:
        return 0


def process_excel(file_name, col_name):
    df =pd.read_excel(file_name, encoding="utf-8", dtype=str)
    df['label'] = df.apply(partial(check_int, col_name=col_name), axis=1)
    df = df[df['label'] == 1]
    return df[col_name]


def output_tsv(file, data, headers=[]):
    with open(file, "w", encoding="utf-8", newline="", ) as fw:
        writer = csv.DictWriter(fw, fieldnames=headers, delimiter="\t")
        writer.writeheader()
        writer.writerows(data)


def output_json(file, data):
    with open(file, "w") as f:
        json.dump(data, f)


def load_csv(file_name, col_name):
    df = pd.read_csv(file_name, encoding='utf8', dtype=str)




def test():
    print(process_excel("nonmatching_subset2017.xlsx", 'ndcnum'))


if __name__ == '__main__':
    test()