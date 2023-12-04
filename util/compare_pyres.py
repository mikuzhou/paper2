import subprocess
import tempfile
import os

def run_code(code):
    try:
        # 创建一个临时文件
        with tempfile.NamedTemporaryFile(delete=False, suffix='.py', mode='w') as tmp_file:
            # 写入要执行的代码
            tmp_file.write(code)
            tmp_file_name = tmp_file.name

        # 使用Python运行临时文件
        result = subprocess.run(['python', tmp_file_name], capture_output=True, text=True)

        # 删除临时文件
        os.remove(tmp_file_name)

        # 返回标准输出和标准错误的组合
        return result.stdout + result.stderr
    except Exception as e:
        # 处理可能发生的任何异常并返回异常信息
        print(f"An error occurred: {e}")
        return None

def compare_code_output(code1, code2):
    try:
        output1 = run_code(code1)
        output2 = run_code(code2)
        if output1 is None or output2 is None:
            return False
        return output1 == output2
    except Exception as e:
        # 处理比较过程中可能发生的异常
        print(f"An error occurred during comparison: {e}")
        return False

