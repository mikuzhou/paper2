import os
import util.write_tocsv
import util.compare_res
import util.immigration
import util.modification
import util.time_compare
import util.compare_pyres
import util.memory_compare
import util.problem_generator
import argparse


def med_time_prob():
    code1 = util.problem_generator.codeGenerator("medium", "time")
    print(code1)
    code2 = util.modification.codeModification(code1, "time")
    if util.compare_pyres.compare_code_output(code1, code2):
        flag = util.time_compare.time_execution(code1, code2)
    else:
        flag = False
    need_to_be_written = [str(flag), "Medium", "Time"]
    return need_to_be_written


def med_mem_prob():
    code1 = util.problem_generator.codeGenerator("medium", "space")
    print(code1)
    code2 = util.modification.codeModification(code1, "space")
    if util.compare_pyres.compare_code_output(code1, code2):
        flag = util.time_compare.time_execution(code1, code2)
    else:
        flag = False
    need_to_be_written = [str(flag), "Medium", "Memory"]
    return need_to_be_written


def hard_time_prob():
    code1 = util.problem_generator.codeGenerator("hard", "time")
    code2 = util.modification.codeModification(code1, "time")
    if util.compare_pyres.compare_code_output(code1, code2):
        flag = util.time_compare.time_execution(code1, code2)
    else:
        flag = False
    need_to_be_written = [str(flag), "Hard", "Time"]
    return need_to_be_written


def hard_mem_prob():
    code1 = util.problem_generator.codeGenerator("hard", "space")
    code2 = util.modification.codeModification(code1, "space")
    if util.compare_pyres.compare_code_output(code1, code2):
        flag = util.time_compare.time_execution(code1, code2)
    else:
        flag = False
    need_to_be_written = [str(flag), "Hard", "Memory"]
    return need_to_be_written


def med_immi():
    code1 = util.problem_generator.codeGenerator("medium", "memory")
    print(code1)
    code2 = util.immigration.codeImmigration(code1, "c++")
    print(code2)
    flag = util.compare_res.compile_and_compare(code2, code1)
    need_to_be_written = [str(flag), "Medium", "ImmiToC++"]
    return need_to_be_written


def hard_immi():
    code1 = util.problem_generator.codeGenerator("hard", "memory")
    code2 = util.immigration.codeImmigration(code1, "c++")
    flag = util.compare_res.compile_and_compare(code2, code1)
    need_to_be_written = [str(flag), "Hard", "ImmiToC++"]
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
    while i < 10:
        print("new round")
        print(i)
        time_data.append(med_time_prob())
        mem_data.append(med_mem_prob())
        try:
            immi_data.append(med_immi())
        except RuntimeError as e:
            immi_data.append(["False", "Medium", "codeToC++"])
        print(time_data)
        print(mem_data)
        print(immi_data)
        i += 1
    i = 0
    while i < 10:
        print("new round")
        print(i)
        time_data.append(hard_time_prob())
        mem_data.append(hard_mem_prob())
        try:
            immi_data.append(med_immi())
        except RuntimeError as e:
            immi_data.append(["False", "Hard", "codeToC++"])
        i += 1
    util.write_tocsv.write_to_csv(file_name1, time_data)
    util.write_tocsv.write_to_csv(file_name2, mem_data)
    util.write_tocsv.write_to_csv(file_name3, immi_data)

    # print(util.fancy_code.pythonCodeGenerator(2,3,4))


if __name__ == '__main__':
    main()
