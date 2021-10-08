import re
class Solution:
    def myAtoi(self, s: str) -> int:
        pattern = r"^ *[+-]?\d+"
        match = re.compile(pattern).match(s) or '0'
        n = int(match[0])
        return -2**31 if n < -2**31 else 2**31 - 1 if n >= 2**31 else n

testcases = [
    {'input': ('42',),              'result': 42},
    {'input': ("   -42",),          'result': -42},
    {'input': ("4193 with words",), 'result': 4193},
    {'input': ("words and 987",),   'result': 0},
    {'input': ("-91283472332",),    'result': -2147483648},
]
from leettest import test
test(Solution().myAtoi, testcases)
