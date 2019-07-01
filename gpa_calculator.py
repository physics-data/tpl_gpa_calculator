#!/usr/bin/python3
# -*- coding: utf-8 -*-

# define your functions or variables here as you wish
# this is only an example!
def get_gpa(level: str):
    if level == 'A':
        return 4.0
    else:
        return 'I forget it'

if __name__ == '__main__':

    # first, get two arguments from command line

    input_file = ''
    output_file = ''

    # read all lines from input, then iterate over it

    input_lines = open(input_file, 'r').readlines()

    gp = {} # sum of grade points
    credit = {} # sum of credits
    count = {} # count of courses

    for line in input_lines:
        # skip empty lines
        # split line into six fields
        # get old/new grades(4.0, 4.0) from level('A')
        # count its credit, grade
        pass

    out = open(output_file, 'w')

    for semester in count:
        # calculate old/new gpa
        # output required information
        out.write('Sem1 1 2 2 4.00 4.00\n')
        pass

    # calculate overall old/new gpa
    # output required information
    out.write('1 1 2 2 4.00 4.00\n')
    
    # close output is a good practice
    out.close()
