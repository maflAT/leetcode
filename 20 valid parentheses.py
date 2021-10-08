"""Given a string s containing just the characters '(', ')', '{', '}', '[' and
']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = set('([{')
        matching = {')': '(', ']': '[', '}': '{'}
        for c in s:
            if c in opening: stack.append(c)
            elif not stack or stack.pop() != matching[c]: return False
        return not stack

testcases = [
    {'input': (r"()",), 'result': True},
    {'input': (r"()[]{}",), 'result': True},
    {'input': (r"(]",), 'result': False},
    {'input': (r"([)]",), 'result': False},
    {'input': (r"{[]}",), 'result': True},
    {'input': (r"}",), 'result': False},
    {'input': (r"[",), 'result': False},
]
from leettest import test
test(Solution().isValid, testcases)
