"""
Given an n x n matrix where each of the rows and columns are sorted in 
ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, 
not the kth distinct element."""

from itertools import chain
class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        return sorted(chain.from_iterable(matrix))[k-1]

testcases = [
    {'input': ([[1,5,9],[10,11,13],[12,13,15]], 8), 'result': 13},
    {'input': ([[-5]], 1), 'result': -5},
]
from leettest import test
test(Solution().kthSmallest, testcases)
