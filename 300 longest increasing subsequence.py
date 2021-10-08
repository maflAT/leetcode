"""Given an integer array `nums`, return the length of the longest strictly
increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some
or no elements without changing the order of the remaining elements. For
example, `[3,6,2,7]` is a subsequence of the array `[0,3,1,6,2,2,7]`."""

class Solution:
    def lengthOfLIS_(self, nums: list[int]) -> int:
        seq_lengths = {1: nums[0]}
        for n in nums:
            for sl in sorted(seq_lengths, reverse=True):
                if n > seq_lengths[sl]:
                    seq_lengths[sl + 1] = min(seq_lengths.get(sl + 1, n), n)
                    continue
                if sl == 1:
                    seq_lengths[1] = n
        return max(seq_lengths.keys())


# Better Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        from bisect import bisect_left
        tail = [nums[0]]
        for n in nums:
            if n > tail[-1]:
                tail.append(n)
            else:
                i = bisect_left(tail, n)
                tail[i] = n
        return len(tail)

testcases = [
    {'input': ([10,9,2,5,3,7,101,18],), 'result': 4},
    {'input': ([0,1,0,3,2,3],), 'result': 4},
    {'input': ([7,7,7,7,7,7,7],), 'result': 1},
]
from leettest import test
test(Solution().lengthOfLIS, testcases)
