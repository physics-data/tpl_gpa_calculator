#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, time, os, subprocess, time, shutil, json

testcases = [
    ('data/gpa_1.in', 'data/gpa_1.out'),
    ('data/gpa_2.in', 'data/gpa_2.out'),
    ('data/gpa_random_1.in', 'data/gpa_random_1.out'),
    ('data/gpa_random_2.in', 'data/gpa_random_2.out'),
    ('data/gpa_random_3.in', 'data/gpa_random_3.out'),
    ('data/gpa_random_4.in', 'data/gpa_random_4.out'),
    ('data/gpa_random_5.in', 'data/gpa_random_5.out'),
    ('data/gpa_random_6.in', 'data/gpa_random_6.out'),
    ('data/gpa_random_7.in', 'data/gpa_random_7.out'),
    ('data/gpa_random_8.in', 'data/gpa_random_8.out'),
]

if __name__ == '__main__':

    if sys.version_info[0] != 3:
        print("Please use python3")
        exit(1)

    program_file = 'gpa_calculator.py'
    
    if not os.path.isfile(program_file):
        print('File {} not present!'.format(program_file))
        exit(1)

    success_count = 0

    for input, output in testcases:
        # remove the output file
        test_filename = 'test.output'
        try:
            os.remove(test_filename)
        except:
            pass
        p = subprocess.Popen([sys.executable, program_file, input, test_filename], stdout=open(os.devnull,'w'), stderr=open(os.devnull,'w'))
        message = ''
        success = True
        start_time = time.time()
        while p.poll() is None:
            if time.time() - start_time > 2:
                p.terminate()
                message = 'Time limit exceeded'
                success = False
        else:
            if not os.path.isfile(test_filename):
                message = 'No output file found'
                success = False
            else:
                std = [line for line in open(output, 'r').readlines() if line.strip()]
                ans = [line for line in open(test_filename, 'r').readlines() if line.strip()]
                if len(std) != len(ans):
                    message = 'Line count mismatch'
                    success = False
                else:
                    for i in range(len(std)):
                        if std[i] != ans[i]:
                            try:
                                parts_std = std[i].split(' ')
                                parts_ans = ans[i].split(' ')
                                float_length = [len(p.strip().split('.')[1]) for p in parts_ans[-2:]]
                                if parts_std[:-2] != parts_ans[:-2] or abs(float(parts_std[-2]) - float(parts_ans[-2])) > 0.011 or abs(float(parts_std[-1]) - float(parts_ans[-1])) > 0.011 or float_length != [2, 2]:
                                    message = 'Line {} mismatch: should be \'{}\', get \'{}\''.format(i, std[i], ans[i])
                                    success = False
                                    break
                            except:
                                message = 'Line {} mismatch: should be \'{}\', get \'{}\''.format(i, std[i], ans[i])
                                success = False
                                break
        if success:
            success_count += 1
            if os.isatty(1):
                print('Testcase {}: PASS'.format(input))
        else:
            if os.isatty(1):
                print('Testcase {}: {}'.format(input, message))
        
        
    grade = int(100.0 * success_count / len(testcases))
    
    if os.isatty(1):
        print('Total Points: {}/100'.format(grade))
    else:
        print(json.dumps({'grade': grade}))

