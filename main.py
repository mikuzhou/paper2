import os
import util.write_tocsv
import util.compare_res
import util.immigration
import util.modification
import util.time_compare
import util.compare_pyres
import util.memory_compare
import util.problem_generator
import collections
import argparse

times = 1

def easy_time_prob():
    global times
    code1 = util.problem_generator.codeGenerator(times, "easy", "time")
    times += 1
    code2 = util.modification.codeModification(code1, "time")
    time_all = [999,999]
    if util.compare_pyres.compare_code_output(code1, code2):
        time_all = util.time_compare.time_execution(code1, code2)
        flag = time_all[0]>time_all[1]
    else:
        flag = False
    need_to_be_written = [str(flag), "Easy", "Time", str(time_all[0]), str(time_all[1])]
    return need_to_be_written


def easy_mem_prob():
    global times
    code1 = util.problem_generator.codeGenerator(times, "easy", "space")
    times += 1
    code2 = util.modification.codeModification(code1, "space")
    mem_all = [999,999]
    if util.compare_pyres.compare_code_output(code1, code2):
        mem_all = util.memory_compare.compare_memory_usage(code1, code2)
        flag = mem_all[0]>mem_all[1]
    else:
        flag = False
    need_to_be_written = [str(flag), "Easy", "Space", str(mem_all[0]), str(mem_all[1])]
    return need_to_be_written

def med_time_prob():
    global times
    code1 = util.problem_generator.codeGenerator(times, "medium", "time")
    times += 1
    code2 = util.modification.codeModification(code1, "time")
    time_all = [999,999]
    if util.compare_pyres.compare_code_output(code1, code2):
        time_all = util.time_compare.time_execution(code1, code2)
        flag = time_all[0]>time_all[1]
    else:
        flag = False
    need_to_be_written = [str(flag), "Medium", "Time", str(time_all[0]), str(time_all[1])]
    return need_to_be_written


def med_mem_prob():
    global times
    code1 = util.problem_generator.codeGenerator(times, "medium", "space")
    times += 1
    code2 = util.modification.codeModification(code1, "space")
    mem_all = [999,999]
    if util.compare_pyres.compare_code_output(code1, code2):
        mem_all = util.memory_compare.compare_memory_usage(code1, code2)
        flag = mem_all[0]>mem_all[1]
    else:
        flag = False
    need_to_be_written = [str(flag), "Medium", "Space", str(mem_all[0]), str(mem_all[1])]
    return need_to_be_written


def hard_time_prob():
    global times
    code1 = util.problem_generator.codeGenerator(times, "hard", "time")
    times += 1
    code2 = util.modification.codeModification(code1, "time")
    time_all = [999,999]
    if util.compare_pyres.compare_code_output(code1, code2):
        time_all = util.time_compare.time_execution(code1, code2)
        flag = time_all[0]>time_all[1]
    else:
        flag = False
    need_to_be_written = [str(flag), "Hard", "Time", str(time_all[0]), str(time_all[1])]
    return need_to_be_written


def hard_mem_prob():
    global times
    code1 = util.problem_generator.codeGenerator(times, "hard", "space")
    times += 1
    code2 = util.modification.codeModification(code1, "space")
    mem_all = [999,999]
    if util.compare_pyres.compare_code_output(code1, code2):
        mem_all = util.memory_compare.compare_memory_usage(code1, code2)
        flag = mem_all[0]>mem_all[1]
    else:
        flag = False
    need_to_be_written = [str(flag), "Hard", "Space", str(mem_all[0]), str(mem_all[1])]
    return need_to_be_written

def easy_immi():
    global times
    code1 = util.problem_generator.codeGenerator(times, "easy", "space")
    times += 1
    code2 = util.immigration.codeImmigration(code1, "c++")
    flag = util.compare_res.compile_and_compare(code2, code1)
    need_to_be_written = [str(flag), "Easy",  "Immigration", "Python", "C++"]
    return need_to_be_written
def med_immi():
    global times
    code1 = util.problem_generator.codeGenerator(times, "medium", "space")
    times += 1
    code2 = util.immigration.codeImmigration(code1, "c++")
    flag = util.compare_res.compile_and_compare(code2, code1)
    need_to_be_written = [str(flag), "Medium",  "Immigration", "Python", "C++"]
    return need_to_be_written


def hard_immi():
    global times
    code1 = util.problem_generator.codeGenerator(times, "hard", "space")
    times += 1
    times+=1
    code2 = util.immigration.codeImmigration(code1, "c++")
    flag = util.compare_res.compile_and_compare(code2, code1)
    need_to_be_written = [str(flag), "Hard",  "Immigration", "Python", "C++"]
    return need_to_be_written


def main():
    # parser = argparse.ArgumentParser(description="Run specified phases of the grading process.")
    # parser.add_argument('--api_key', default=None,
    #                     help="your api_key")
    # args = parser.parse_args()
    # if args.api_key:
    #     openai_api_key = args.api_key
    i = 0
    file_name1 = "time.csv"
    file_name2 = "mem.csv"
    file_name3 = "immi.csv"
    time_data = []
    mem_data = []
    immi_data = []
    while i < 5:
        print("new round")
        print(i)
        mem_data.append(easy_mem_prob())
        time_data.append(easy_time_prob())

        try:
            immi_data.append(easy_immi())
        except RuntimeError as e:
            immi_data.append(["False", "Easy", "Immigration", "Python", "C++"])
        print(time_data)
        print(mem_data)
        print(immi_data)
        i += 1
    i = 0
    while i < 5:
        print("new round")
        print(i)
        mem_data.append(med_mem_prob())
        time_data.append(med_time_prob())

        try:
            immi_data.append(med_immi())
        except RuntimeError as e:
            immi_data.append(["False", "Medium", "Immigration", "Python", "C++"])
        print(time_data)
        print(mem_data)
        print(immi_data)
        i += 1
    i = 0
    while i < 5:
        print("new round")
        print(i)
        time_data.append(hard_time_prob())
        mem_data.append(hard_mem_prob())
        try:
            immi_data.append(med_immi())
        except RuntimeError as e:
            immi_data.append(["False", "Hard",  "Immigration", "Python", "C++"])
        i += 1
    util.write_tocsvcmp.write_to_csv(file_name1, time_data)
    util.write_tocsvcmp.write_to_csv(file_name2, mem_data)
    util.write_tocsvcmp.write_to_csv(file_name3, immi_data)

    # print(util.fancy_code.pythonCodeGenerator(2,3,4))


if __name__ == '__main__':
    main()
