import time

def time_execution(code1, code2, setup=""):
    """
    Function to time and compare the execution of two code snippets.
    """
    # 记录第一段代码的执行时间
    start_time = time.time()
    exec(code1)
    time1 = time.time() - start_time

    # 记录第二段代码的执行时间
    start_time = time.time()
    exec(code2)
    time2 = time.time() - start_time
    time_all = []
    time_all.append(time1)
    time_all.append(time2)
    return time_all
