from memory_profiler import memory_usage

def compare_memory_usage(code1, code2):
    # 评估第一段代码的内存使用
    mem_usage_code1 = memory_usage((exec, (code1,), {}))
    max_usage_code1 = max(mem_usage_code1)

    # 评估第二段代码的内存使用
    mem_usage_code2 = memory_usage((exec, (code2,), {}))
    max_usage_code2 = max(mem_usage_code2)

    # 如果code1的内存使用更小，则返回True
    return max_usage_code1 >= max_usage_code2