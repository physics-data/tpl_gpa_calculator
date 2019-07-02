#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, os, random, string

from std import calculate_gpa, gpa_map

semester_prefix = list(range(1, 10))
semester_year = list(range(2010, 2020))
grade_list = list(gpa_map.items())

abnormal_grade_list = [
    ('P', 'N/A'),
    ('I', 'N/A'),
    ('EX', 'N/A'),
    ('W', 'N/A'),
    ('***', '***')
]

def random_item():
    course_id = ''.join(random.choice(string.digits) for i in range(8))
    course_name = ''.join(random.choice(string.ascii_lowercase) for i in range(6))
    credit = int(course_id[-1])

    if random.uniform(0, 1) > 0.95:
        level, points = random.choice(abnormal_grade_list)
    else:
        level, (old, new) = random.choice(grade_list)
        points = f'{new / 10:.1f}'

    semester = f'{random.choice(semester_year)}_{random.choice(semester_prefix)}'
    return f'{course_id}\t{course_name}\t{credit}\t{level}\t{points}\t{semester}\n'


def generate_gpa(input_file, problem_size):
    f = open(input_file, 'w')
    for _ in range(problem_size):
        f.write(random_item())


problem_size = [10, 10, 100, 100, 1000, 1000, 10000, 10000]


if __name__ == '__main__':

    os.makedirs('data', exist_ok=True)
    
    for i in range(8):
        input_file = f'data/gpa_random_{i+1}.in'
        output_file = f'data/gpa_random_{i+1}.out'
        generate_gpa(input_file, problem_size[i])
        calculate_gpa(input_file, output_file)
