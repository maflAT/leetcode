"""Given an array nums of n integers, return an array of all the unique
quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

    0 <= a, b, c, d < n a, b, c, and d are distinct. nums[a] + nums[b] +
    nums[c] + nums[d] == target"""

class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        n = len(nums)
        quads = set()
        for a in range(n):
            for b in range(a + 1, n):
                for c in range(b + 1, n):
                    for d in range(c + 1, n):
                        if nums[a] + nums[b] + nums[c] + nums[d] == target:
                            quads.add(tuple(sorted([nums[a], nums[b], nums[c], nums[d]])))
        return [list(t) for t in quads]

testcases = [
    {'input': ([1,0,-1,0,-2,2],0), 'result': [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]},
    {'input': ([2,2,2,2,2],8), 'result': [[2,2,2,2]]},
    {'input': ([-5,5,4,-3,0,0,4,-2], 4), 'result': [[-5,0,4,5],[-3,-2,4,5]]},
    {'input': ([-444,-400,-398,-387,-372,-347,-340,-337,-330,-326,-326,-308,
        -304,-295,-270,-228,-224,-213,-196,-192,-186,-118,-103,-92,-89,-42,-31,
        -28,-20,-19,-8,1,1,9,48,49,74,88,90,135,152,160,170,181,181,202,238,254,
        271,272,274,285,287,302,314,319,342,373,373,392,400,453,482],-4402), 
        'result': []},
]
from leettest import test
test(Solution().fourSum, testcases)
