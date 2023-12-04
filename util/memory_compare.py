from memory_profiler import memory_usage

def compare_memory_usage(code1, code2):
    try:
        # 评估第一段代码的内存使用
        mem_usage_code1 = memory_usage((exec, (code1,), {}))
        max_usage_code1 = round(max(mem_usage_code1))

        # 评估第二段代码的内存使用
        mem_usage_code2 = memory_usage((exec, (code2,), {}))
        max_usage_code2 = round(max(mem_usage_code2))

        return [max_usage_code1, max_usage_code2]
    except Exception as e:
        # 如果执行代码时发生异常，返回默认值
        print(e)
        return [999, 999]
