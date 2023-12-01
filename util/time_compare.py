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

    if time1>=time2:
        return True
    else:
        return False
