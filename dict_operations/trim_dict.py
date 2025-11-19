#!/usr/bin/env python3
import csv

with open('dict.csv', 'r', encoding='utf-8') as infile, \
     open('words.txt', 'w', encoding='utf-8') as outfile:

    reader = csv.reader(infile)
    next(reader)  # skip header

    for row in reader:
        if row:  # skip empty rows
            outfile.write(row[0] + '\n')

print("Done! Created words.txt")
