#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, time, os, subprocess, time

testcases = [
    ('examples/gpa.in', 'examples/gpa.out'),
]

if __name__ == '__main__':

    if sys.version_info[0] != 3:
        print("Please use python3")
        exit(1)
    
    if not os.path.isfile('gpa_calculator.py'):
        print('gpa_calculator.py not present!')
        exit(1)

    os.makedirs('test', exist_ok=True)

    for input, output in testcases:

        test_filename = 'test/test.output'
        p = subprocess.Popen(['python3', 'gpa_calculator.py', input, test_filename], stdout=open(os.devnull,'w'), stderr=open(os.devnull,'w'))
        message = ''
        success = True
        start_time = time.time()
        while p.poll() is None:
            if time.time() - start_time > 2000:
                p.terminate()
                message = 'Time Limit Exceeded'
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
                            message = f'Line {i} mismatch: should be \'{std[i]}\', get \'{ans[i]}\''
                            success = False
                            break

        if success:
            print(f'Testcase {input}: PASS')
        else:
            print(f'Testcase {input}: {message}')
        
        
