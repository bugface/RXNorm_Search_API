from query_api import ndc_allRelated
from data_utils import process_excel, output_tsv, output_json
from config import input_file, ndc_col, output_file, json_output
import argparse


def rxcui2ingredient():
    pass


def


def main():
    # arguments
    arg_parser = argparse.ArgumentParser(description='process input files, column names, outputs and models')
    arg_parser.add_argument("-i", "-input", help="input file (excel, csv or tsv) with the header", type=str)
    args = arg_parser.parse_args()

    res = []
    ndc_codes = process_excel(input_file, ndc_col)
    for code in ndc_codes:
        res.append(ndc_allRelated(code))

    fields = set()
    for each in res:
        for k in each:
            fields.add(k)
    base_dict = {k: None for k in fields}

    n_res = []
    for each in res:
        # for k, v in each.items():
        #     if str(v).startswith("0"):
        #         each[k] = '{}s'.format(v)
        n_res.append({**base_dict, **each})

    output_tsv(output_file, n_res, fields)
    output_json(json_output, n_res)


if __name__ == '__main__':
    main()

