#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, time, os, subprocess, time, shutil, json

testcases = [
    ('examples/gpa.in', 'examples/gpa.out'),
]

if __name__ == '__main__':

    if sys.version_info[0] != 3:
        print("Please use python3")
        exit(1)

    program_file = 'gpa_calculator.py'
    
    if not os.path.isfile(program_file):
        print(f'File {program_file} not present!')
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
                                if parts_std[:-2] != parts_ans[:-2] or abs(float(parts_std[-2]) - float(parts_ans[-2])) > 0.011 or abs(float(parts_std[-1]) - float(parts_ans[-1])) > 0.011:
                                    message = f'Line {i} mismatch: should be \'{std[i]}\', get \'{ans[i]}\''
                                    success = False
                                    break
                            except:
                                message = f'Line {i} mismatch: should be \'{std[i]}\', get \'{ans[i]}\''
                                success = False
                                break
        if success:
            success_count += 1
            if os.isatty(1):
                print(f'Testcase {input}: PASS')
        else:
            if os.isatty(1):
                print(f'Testcase {input}: {message}')
        
        
    grade = int(100.0 * success_count / len(testcases))
    
    if os.isatty(1):
        print(f'Total Points: {grade}/100')
    else:
        print(json.dumps({'grade': grade}))

