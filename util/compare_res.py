import subprocess
import os
import uuid

def compile_and_compare(cpp_code, python_code):
    def write_and_compile_cpp(cpp_code_str, filename):
        with open(f"{filename}.cpp", "w") as file:
            file.write(cpp_code_str)
        # 检查编译过程是否成功
        try:
            subprocess.run(["g++", f"{filename}.cpp", "-o", filename], check=True)
        except subprocess.CalledProcessError:
            raise RuntimeError("Compilation failed")

    def execute_and_get_output(command, input="", shell=False):
        process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=shell)
        stdout, stderr = process.communicate(input)
        if process.returncode != 0:
            raise RuntimeError(f"Error executing command: {stderr}")
        return stdout.strip()

    filename = f"temp_cpp_program_{uuid.uuid4().hex}"

    try:
        write_and_compile_cpp(cpp_code, filename)
        cpp_output = execute_and_get_output([f"./{filename}"], shell=True)
        python_output = execute_and_get_output(["python", "-c", python_code])
        return cpp_output == python_output

    finally:
        if os.path.exists(f"{filename}.cpp"):
            os.remove(f"{filename}.cpp")
        if os.path.exists(filename):
            os.remove(filename)


