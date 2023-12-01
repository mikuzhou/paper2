import io
import sys
from contextlib import redirect_stdout

def capture_output(code):
    f = io.StringIO()
    with redirect_stdout(f):
        exec(code)
    return f.getvalue()

def compare_code_output(code1, code2):
    output1 = capture_output(code1)
    output2 = capture_output(code2)
    return output1 == output2
