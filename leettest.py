import re
from typing import Any, Callable, Iterable

"""
testcases = [
    {'input': (), 'result': },
]
from leettest import test
test(func, testcases)
"""

def test(func: Callable, testcases: list[tuple, Any], break_on_error: bool=False) -> bool:
    pass_ = True
    for tc in testcases:
        arg_str = arg_format(tc['input'], length=50)
        expr = f"{func.__name__}({arg_str})"
        return_value = func(*tc['input'])
        if return_value == tc['result']:
            print(f"{expr} = {return_value}")
        else:
            print(f"\nTEST FAILED:",
                  f"{expr} =",
                  f"returned: {return_value}",
                  f"expected: {tc['result']}", sep='\n')
            if break_on_error: return False
            else: pass_ = False
    return pass_

def arg_format(args: Iterable, length: int=0) -> str:
    arg_str = ', '.join(map(str, list(args)))
    if not length or length > len(arg_str): return arg_str
    if arg_str[0] in '({[':
        pattern = r"^([\(\[\{\s]*)(.*?)([\)\]\}\s]*)$"
        matches = re.compile(pattern, re.DOTALL).match(arg_str)
        try:
            beginning, middle, end = matches.groups()
            length = max(0, length - len(beginning) - len(end))
            return beginning + middle[:length] + '...' + end
        except (TypeError, IndexError):
            pass
    if length < 5: return arg_str[:length]
    else: return arg_str[:length - 3] + '...'
