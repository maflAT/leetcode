"""Given a string s, find the length of the longest substring without repeating
characters."""

from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        previous_occurrence = defaultdict(int)
        longest_chain = current_chain = 0
        for pos, c in enumerate(s, 1):
            dist = pos - previous_occurrence[c]
            previous_occurrence[c] = pos
            if dist > current_chain:
                current_chain += 1
            else:
                current_chain = dist
            longest_chain = max(longest_chain, current_chain)
        return longest_chain

testcases = [
    {'input': ("",), 'result': 0},
    {'input': ("a",), 'result': 1},
    {'input': ("aa",), 'result': 1},
    {'input': ("ab",), 'result': 2},
    {'input': ("aba",), 'result': 2},
    {'input': ("abb",), 'result': 2},
    {'input': ("aab",), 'result': 2},
    {'input': ("abcabcbb",), 'result': 3},
    {'input': ("bbbbb",), 'result': 1},
    {'input': ("pwwkew",), 'result': 3},
]
from leettest import test
test(Solution().lengthOfLongestSubstring, testcases)