"""
A message containing letters from `A-Z` can be encoded into numbers using the
following mapping:

'A' -> "1" 'B' -> "2"
...
'Z' -> "26"

To decode an encoded message, all the digits must be grouped then mapped back
into letters using the reverse of the mapping above (there may be multiple
ways). For example, `"11106"` can be mapped into:

    `"AAJF"` with the grouping `(1 1 10 6)`
    `"KJF"` with the grouping `(11 10 6)`

Note that the grouping `(1 11 06)` is invalid because `"06"` cannot be mapped
into `'F'` since `"6"` is different from `"06"`.

In addition to the mapping above, an encoded message may contain the `'*'`
character, which can represent any digit from `'1'` to `'9'` (`'0'` is
excluded). For example, the encoded message `"1*"` may represent any of the
encoded messages `"11"`, `"12"`, `"13"`, `"14"`, `"15"`, `"16"`, `"17"`,
`"18"`, or `"19"`. Decoding `"1*"` is equivalent to decoding any of the encoded
messages it can represent.

Given a string s containing digits and the `'*'` character, return the number
of ways to decode it.

Since the answer may be very large, return it modulo `1_000_000_007`.
"""

CYPHER = None
LENGTH = None
cache = {}
class Solution:
    def numDecodings(self, s: str) -> int:
        global CYPHER, LENGTH, cache
        CYPHER = s
        LENGTH = len(s)
        cache = {}
        return decode(0)

def cached(f):
    global cache
    MOD = 10**9 + 7
    def wrapper(*args):
        if args not in cache: 
            res = f(*args)
            cache[args] = res if res < MOD else res % MOD
        return cache[args]
    return wrapper

@cached
def decode(i: int):
    global CYPHER, LENGTH
    if i >= LENGTH: return 1
    if CYPHER[i] == '0': return 0
    if i + 1 == LENGTH:
        if CYPHER[i] == '*': return 9
        return 1
    if CYPHER[i] == '1':
        if CYPHER[i + 1] == '0': return decode(i + 2)
        if CYPHER[i + 1] == '*': return decode(i + 1) + 9 * decode(i + 2)
        return decode(i + 1) + decode(i + 2)
    if CYPHER[i] == '2':
        if CYPHER[i + 1] == '0': return decode(i + 2)
        if CYPHER[i + 1] == '*': return decode(i + 1) + 6 * decode(i + 2)
        if CYPHER[i + 1] in '789': return decode(i + 1)
        return decode(i + 1) + decode(i + 2)
    if CYPHER[i] == '*':
        if CYPHER[i + 1] == '0': return 2 * decode(i + 2)
        if CYPHER[i + 1] == '*': return 9 * decode(i + 1) + 15 * decode(i + 2)
        if CYPHER[i + 1] in '789': return 9 * decode(i + 1) + decode(i + 2)
        return 9 * decode(i + 1) + 2 * decode(i + 2)
    return decode(i + 1)


#memory limit exceeded
# @cached
# def decode_(s: str):
#     if len(s) == 0: return 1
#     if s[0] == '0': return 0
#     if len(s) == 1:
#         if s[0] == '*': return 9
#         if s[0] in '123456789': return 1
#     if len(s) > 1:
#         if s[0] == '1':
#             if s[1] == '0': return decode(s[2:])
#             if s[1] == '*': return decode(s[1:]) + 9 * decode(s[2:])
#             if s[1] in '123456789': return decode(s[1:]) + decode(s[2:])
#         if s[0] == '2':
#             if s[1] == '0': return decode(s[2:])
#             if s[1] == '*': return decode(s[1:]) + 6 * decode(s[2:])
#             if s[1] in '789': return decode(s[1:])
#             if s[1] in '123456': return decode(s[1:]) + decode(s[2:])
#         if s[0] == '*':
#             if s[1] == '0': return 2 * decode(s[2:])
#             if s[1] == '*': return 9 * decode(s[1:]) + 15 * decode(s[2:])
#             if s[1] in '789': return 9 * decode(s[1:]) + decode(s[2:])
#             if s[1] in '123456': return 9 * decode(s[1:]) + 2 * decode(s[2:])
#         if s[0] in '3456789': return decode(s[1:])
#     raise Exception(f'This should not be reachable!\n{s = }')

testcases = [
    {'input': ("*",), 'result': 9},
    {'input': ("1*",), 'result': 18},
    {'input': ("2*",), 'result': 15},
    {'input': ("*7",), 'result': 10},
    {'input': ("1*7",), 'result': 19},
    {'input': ("1*72*",), 'result': 285},
]
from leettest import test
test(Solution().numDecodings, testcases)
