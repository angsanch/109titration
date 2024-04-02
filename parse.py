#!/usr/bin/env python3
##
## EPITECH PROJECT, 2024
## EPITECH PROJECT 109TITRATION
## File description:
## parse the csv
##

import sys
import csv
from collections import defaultdict

def open_file():
    file = open(sys.argv[1], 'r')
    csvreader = csv.reader(file, delimiter=';')
    columns = defaultdict(list)

    for row in csvreader:
        if len(row) != 2:
            raise Exception("number of columns given in the csv is wrong")
        for i in range(2):
            columns[i].append(float(row[i]))
    return columns

def parse_information():
    file_data = open_file()
    data = {
        "vol": file_data[0],
        "pH": file_data[1],
    }
    return data
