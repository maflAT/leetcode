from collections import Counter
import math
class Solution:
    def minSetSize(self, arr: list[int]) -> int:
        length = len(arr)
        rest = math.ceil(length / 2)
        set_size = 0
        for _, n in Counter(arr).most_common(length // 2 + 1):
            set_size += 1
            rest -= n
            if rest <= 0: return set_size


testcases = [
    {'input': ([3,3,3,3,5,5,5,2,2,7],),  'result': 2},
    {'input': ([7,7,7,7,7,7],),          'result': 1},
    {'input': ([1,9],),                  'result': 1},
    {'input': ([1000,1000,3,7],),        'result': 1},
    {'input': ([1,2,3,4,5,6,7,8,9,10],), 'result': 5},
]
from leettest import test
test(Solution().minSetSize, testcases)