#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys

# define your functions or variables here as you wish
# this is only an example!
gp_map = {
    'A+': [40, 40],
    'A': [40, 40],
    'A-': [37, 40],
    'B+': [33, 36],
    'B': [30, 33],
    'B-': [27, 30],
    'C+': [23, 26],
    'C': [20, 23],
    'C-': [17, 20],
    'D+': [13, 16],
    'D': [10, 13],
    'F': [0, 0]
}

# main entry
if __name__ == '__main__':

    # first, get two arguments from command line

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # read all lines from input, then iterate over it

    input_lines = open(input_file, 'r').read().splitlines()

    # gps = {}  # sum of grade points: sem_name -> [gps_old, gps_new]
    # credit = {}  # sum of credits: sem_name -> [credit, gp_credit]
    # count = {}  # count of courses: sem_name -> int
    data = {}  # sem_name -> [count, credit, gp_credit, gps_old, gps_new]

    for line in input_lines:
        # skip empty lines
        # split line into six fields
        # get old/new grades(4.0, 4.0) from level('A')
        # count its credit, grade
        line.strip()
        if(len(line) < 6):
            continue

        [cid, cname, cred, lvl, gp_n, sem] = line.split('\t')
        cred = int(cred)
        if(not (sem in data)):
            data[sem] = [0, 0, 0, 0, 0]

        gpp = gp_map.get(lvl, None)

        data[sem][0] += 1
        data[sem][1] += cred

        if(gpp != None):    # normal course
            data[sem][2] += cred
            data[sem][3] += cred * gpp[0]
            data[sem][4] += cred * gpp[1]

    out = open(output_file, 'w')

    total_data = [0, 0, 0, 0, 0]

    for sem, value in data.items():
        # calculate old/new gpa
        # output required information
        out.write('{} {:.0f} {:.0f} {:.0f} {:.2f} {:.2f}\n'.format(
            sem,        # sem name
            value[0],   # course count
            value[1],   # total credit
            value[2],   # total gpa credit
            value[3] / 10.0 / value[2]  if value[2] > 0 else -1.0,   # old GPA
            value[4] / 10.0 / value[2] if value[2] > 0 else -1.0    # new GPA
        ))

        for i in range(5):
            total_data[i] += value[i]

    # calculate overall old/new gpa
    # output required information
    out.write('{} {:.0f} {:.0f} {:.0f} {:.2f} {:.2f}\n'.format(
        len(data),       # sem count
        total_data[0],   # course count
        total_data[1],   # total credit
        total_data[2],   # total gpa credit
        total_data[3] / total_data[2] / \
        10.0 if total_data[2] > 0 else -1.0,  # old GPA
        total_data[4] / total_data[2] / \
        10.0 if total_data[2] > 0 else -1.0   # new GPA
    ))

    # close output is a good practice
    out.close()
