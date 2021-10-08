"""Given an array nums of positive integers, call a (contiguous, not
necessarily distinct) subarray of nums good if the number of different integers
in that subarray is exactly k.

(For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.)

Return the number of good subarrays of nums."""

from collections import defaultdict
from itertools import count
class Solution:
    # solution with swap cache instead of dict copy (10x faster)
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        occurances = defaultdict(int)
        swap = defaultdict(int)
        tail = array_count = 0
        for head in range(len(nums)):
            occurances[nums[head]] += 1
            if len(occurances) > k:
                for tail in count(tail):
                    num = nums[tail]
                    if occurances[num] <= 1: 
                        del occurances[num]
                        tail += 1
                        break
                    occurances[num] -= 1
            if len(occurances) == k:
                swap.clear()
                for i in count(tail):
                    array_count += 1
                    num = nums[i]
                    if occurances[num] <= 1: 
                        for n, cnt in swap.items(): occurances[n] += cnt
                        break
                    occurances[num] -= 1
                    swap[num] += 1
        return array_count

    # def _subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
    #     occurances = defaultdict(int)
    #     tail = sub_count = 0
    #     for head in range(len(nums)):
    #         occurances[nums[head]] += 1
    #         if len(occurances) > k:
    #             for tail in count(tail):
    #                 num = nums[tail]
    #                 if occurances[num] > 1: 
    #                     occurances[num] -= 1
    #                 else: 
    #                     del occurances[num]
    #                     tail += 1
    #                     break
    #         if len(occurances) == k:
    #             occurances_ = occurances.copy()
    #             for i in count(tail):
    #                 sub_count += 1
    #                 num = nums[i]
    #                 if occurances_[num] > 1: 
    #                     occurances_[num] -= 1
    #                 else: 
    #                     # del occurances_[num]
    #                     break
    #     return sub_count

testcases = [
    {'input': ([1,2,1,2,3], 2), 'result': 7},
    {'input': ([1,2,1,3,4], 3), 'result': 3},
    {'input': ([1,2], 1), 'result': 2},
    {'input': ([9], 1), 'result': 1},
    {'input': ([1,1,1], 1), 'result': 6},
]
from leettest import test
test(Solution().subarraysWithKDistinct, testcases)
