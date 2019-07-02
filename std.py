#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, os
from decimal import *

# ten times for integer calculation
gpa_map = {
    'A+': (40, 40),
    'A':  (40, 40),
    'A-': (37, 40),
    'B+': (33, 36),
    'B':  (30, 33),
    'B-': (27, 30),
    'C+': (23, 26),
    'C':  (20, 23),
    'C-': (17, 20),
    'D+': (13, 16),
    'D':  (10, 13),
    'F':  (00, 00),
}

ignore_grades = ['W', 'P', 'EX', 'I', '***']


def calculate_gpa(input_file, output_file):
    old_gp = {}
    new_gp = {}
    credits = {}
    credits_gpa = {}
    counts = {}
    counts_gpa = {}

    gpa_lines = open(input_file, 'r').readlines()

    for line in gpa_lines:
        # skip empty lines
        line = line.strip()
        if line == '':
            continue
        # retrieve fields
        fields = line.split('\t')
        credit = int(fields[2])
        semester = fields[5]
        level = fields[3]

        # decide if course counts in GPA
        calculate_gpa = False
        old_new = 0, 0
        if not level in ignore_grades:
            calculate_gpa = True
            old, new = gpa_map[level]

        # insert into map
        if not semester in counts:
            credits[semester] = credit
            counts[semester] = 1
            credits_gpa[semester] = credit if calculate_gpa else 0
            old_gp[semester] = old * credit if calculate_gpa else 0
            new_gp[semester] = new * credit if calculate_gpa else 0
        else:
            credits[semester] += credit
            counts[semester] += 1
            credits_gpa[semester] += credit if calculate_gpa else 0
            old_gp[semester] += old * credit if calculate_gpa else 0
            new_gp[semester] += new * credit if calculate_gpa else 0

    out = open(output_file, 'w')

    getcontext().prec = 100
    quantize_prec = Decimal(10) ** -2
    
    for semester in counts:
        # calculate and output this year
        count = counts[semester]
        credit = credits_gpa[semester]
        if credit == 0:
            old_gpa, new_gpa = -1.0, -1.0
        else:
            old_gpa = (Decimal(old_gp[semester]) / Decimal(10 * credit)).quantize(quantize_prec, rounding=ROUND_HALF_UP)
            new_gpa = (Decimal(new_gp[semester]) / Decimal(10 * credit)).quantize(quantize_prec, rounding=ROUND_HALF_UP)
        out.write(f'{semester} {count} {credits[semester]} {credit} {old_gpa} {new_gpa}\n')

    # print summary
    count, credit, old, new = sum(counts.values()), sum(credits_gpa.values()), sum(old_gp.values()), sum(new_gp.values())
    old_gpa = (Decimal(old) / Decimal(10 * credit)).quantize(quantize_prec, rounding=ROUND_HALF_UP)
    new_gpa = (Decimal(new) / Decimal(10 * credit)).quantize(quantize_prec, rounding=ROUND_HALF_UP)
    out.write(f'{len(counts)} {count} {sum(credits.values())} {credit} {old_gpa} {new_gpa}\n')


if __name__ == '__main__':

    if len(sys.argv) != 3:
        print(f'Usage: {sys.argv[0]} input_file output_file')
        exit(1)

    if not os.path.isfile(sys.argv[1]):
        print(f'Input file {sys.argv[1]} not existed')
        exit(1)

    calculate_gpa(sys.argv[1], sys.argv[2])
