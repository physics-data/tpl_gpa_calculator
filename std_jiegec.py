#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from collections import OrderedDict

# define your functions or variables here as you wish
# this is only an example!
def get_gpa(level: str):
    if level == 'A+':
        return (40, 40)
    elif level == 'A':
        return (40, 40)
    elif level == 'A-':
        return (37, 40)
    elif level == 'B+':
        return (33, 36)
    elif level == 'B':
        return (30, 33)
    elif level == 'B-':
        return (27, 30)
    elif level == 'C+':
        return (23, 26)
    elif level == 'C':
        return (20, 23)
    elif level == 'C-':
        return (17, 20)
    elif level == 'D+':
        return (13, 16)
    elif level == 'D':
        return (10, 13)
    elif level == 'F':
        return (0, 0)
    else:
        return None

# main entry
if __name__ == '__main__':

    # first, get two arguments from command line

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # read all lines from input, then iterate over it

    input_lines = open(input_file, 'r').readlines()

    gp_old = OrderedDict() # sum of grade points
    gp_new = OrderedDict() # sum of grade points
    credit = OrderedDict() # sum of credits
    gpa_credit = OrderedDict() # sum of credits
    count = OrderedDict() # count of courses

    for line in input_lines:
        # skip empty lines
        # split line into six fields
        # get old/new grades(4.0, 4.0) from level('A')
        # count its credit, grade
        line = line.strip()
        if len(line) == 0:
            pass
        fields = line.split('\t')
        gpa = get_gpa(fields[3])
        name = fields[5]

        if name not in gp_old:
            gp_old[name] = 0
        if name not in gp_new:
            gp_new[name] = 0
        if name not in credit:
            credit[name] = 0
        if name not in gpa_credit:
            gpa_credit[name] = 0
        if name not in count:
            count[name] = 0

        count[name] += 1
        credit[name] += int(fields[2])
        if gpa != None:
            old, new = gpa
            gp_old[name] += old * int(fields[2])
            gp_new[name] += new * int(fields[2])
            gpa_credit[name] += int(fields[2])

    out = open(output_file, 'w')

    total_courses = 0
    total_credit = 0
    total_gpa_credit = 0
    total_gpa_new = 0
    total_gpa_old = 0
    for sem in count:
        # calculate old/new gpa
        # output required information
        total_courses += count[sem]
        total_credit += credit[sem]
        total_gpa_credit += gpa_credit[sem]
        total_gpa_new += gp_new[sem]
        total_gpa_old += gp_old[sem]
        if gpa_credit[sem] != 0:
            out.write('%s %d %d %d %.2f %.2f\n' % (sem, count[sem], credit[sem], gpa_credit[sem], round(gp_old[sem] / gpa_credit[sem] / 10.0, 2), round(gp_new[sem] / gpa_credit[sem] / 10.0, 2)))
        else:
            out.write('%s %d %d %d %.2f %.2f\n' % (sem, count[sem], credit[sem], gpa_credit[sem], -1.0, -1.0))

    # calculate overall old/new gpa
    # output required information
    out.write('%d %d %d %d %.2f %.2f\n' % (len(count), total_courses, total_credit, total_gpa_credit, round(total_gpa_old / total_gpa_credit / 10.0, 2), round(total_gpa_new / total_gpa_credit / 10.0, 2)))
    
    # close output is a good practice
    out.close()
