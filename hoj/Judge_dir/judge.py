import os
import sys
import time
import filecmp
import shutil

IN_FILE = 'Judge_dir/temp/hidden_in.txt'
OUT_FILE = 'Judge_dir/temp/hidden_out.txt'
CODE_FILE = 'Judge_dir/temp/test'
USER_FILE = 'Judge_dir/temp/user_out.txt'

#(0, 'Pending'),
#(1, 'Accepted'),
#(2, 'Wrong Answer'),
#(3, 'Compilation Error'),
#(4, 'Time Limit Exceeded'),
#(5, 'Memory Limit Exceeded'),
#(6, 'Run Time Error'),
# command < IN_FILE > OUT_FILE

#straight forward file comparison
#need to improve
def compare():
    f1 = open(OUT_FILE)
    f2 = open(USER_FILE)
    if f1.read() == f2.read():
        return 1
    else:
        return 2

def c_lang(code, time_limit, memory_limit):
    compile_ = 'gcc ' + code
    #try:
    com = os.system(compile_)
    if com != 0:
        return 3, 0
    else:
        run = 'timeout ' + str(time_limit) + 's ' + './a.out' + '< ' + IN_FILE  + ' > ' + USER_FILE
        start_time = time.time()
        ret = os.system(run) #return 0 on success, TLE 31744, 34816 on RTE
        end_time = time.time()
        execution_time = end_time - start_time
        if ret == 31744:
            return 4, execution_time
        elif ret == 34816:
            return 6, execution_time
        else:
            return compare(), execution_time


def cpp_lang(code, time_limit, memory_limit):
    compile_ = 'g++ ' + code
    #try:
    com = os.system(compile_)
    if com != 0:
        return 3, 0
    else:
        run = 'timeout ' + str(time_limit) + 's ' + './a.out' + '< ' + IN_FILE  + ' > ' + USER_FILE
        start_time = time.time()
        ret = os.system(run) #return 0 on success, TLE 31744, 34816 on RTE
        end_time = time.time()
        execution_time = end_time - start_time
        if ret == 31744:
            return 4, execution_time
        elif ret == 34816:
            return 6, execution_time
        else:
            return compare(), execution_time

def python_lang(code, time_limit, memory_limit):
    compile_ = 'python -m py_compile ' + code
    #try:
    com = os.system(compile_)
    if com != 0:
        return 3, 0
    else:
        run = 'timeout ' + str(time_limit) + 's ' + 'python ' + code.split('.')[0] + '.pyc' + '< ' + IN_FILE  + ' > ' + USER_FILE
        start_time = time.time()
        ret = os.system(run) #return 0 on success, otherwise 31744
        end_time = time.time()
        execution_time = end_time - start_time
        if ret == 31744:
            return 4, execution_time
        elif ret == 34816:
            return 6, execution_time
        else:
            return compare(), execution_time


def judging(in_file_path, out_file_path, code_file_path, language, time_limit, memory_limit):
    #Temp dir
    os.mkdir('Judge_dir/temp/')
    #copy files to the curent directory
    extension = code_file_path.split('.')[1]
    code = CODE_FILE + '.' + extension
    shutil.copy(in_file_path, IN_FILE)
    shutil.copy(out_file_path, OUT_FILE)
    shutil.copy(code_file_path, code)

	#memory_limit have not implemented
	#no security check
    if language == 'C':
        v, t = c_lang(code, time_limit, memory_limit)
    elif language == 'C++':
        v, t = cpp_lang(code, time_limit, memory_limit)
    elif language == 'Python':
        v, t = python_lang(code, time_limit, memory_limit)
    
    shutil.rmtree('Judge_dir/temp/')
    return v,t
