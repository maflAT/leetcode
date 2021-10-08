class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        def bisect(start: int, stop:int) -> int:
            nonlocal arr, x
            if x <= arr[start]:  return start
            if x >= arr[stop]:   return stop
            center = start + (stop - start) // 2
            if arr[center] == x: return center
            if arr[center] > x:  return bisect(start, center)
            if arr[center] < x:  return bisect(center + 1, stop)

        position = bisect(0, len(arr) - 1)
        neighbors = arr[max(0, position - k):min(position + k, len(arr))]
        neighbors.sort(key=lambda n: abs(n - x))
        return sorted(neighbors[:k])


testcases = [
    {'input': ([1,2,3,4,5], 4, -1),     'result': [1,2,3,4]},
    {'input': ([1,2,3,4,5], 4, 0),      'result': [1,2,3,4]},
    {'input': ([1,2,3,4,5], 4, 1),      'result': [1,2,3,4]},
    {'input': ([1,2,3,4,5], 4, 2),      'result': [1,2,3,4]},
    {'input': ([1,2,3,4,5], 4, 3),      'result': [1,2,3,4]},
    {'input': ([1,2,3,4,5], 4, 4),      'result': [2,3,4,5]},
    {'input': ([1,2,3,4,5], 4, 5),      'result': [2,3,4,5]},
    {'input': ([1,2,3,4,5], 4, 6),      'result': [2,3,4,5]},
    {'input': ([1,1,1,10,10,10], 1, 9), 'result': [10]},
]

from leettest import test
test(Solution().findClosestElements, testcases)