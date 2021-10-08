class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        return hashmap(nums, target)

def hashmap(nums: list[int], target: int):
    duplicates = set()
    s = set()
    for n in nums:
        if n in s: duplicates.add(n)
        s.add(n)
    for n in duplicates:
        if target - n in s: 
            i1 = nums.index(n)
            i2 = nums.index(n, i1 + 1)
            return [i1, i2]
    for n in s:
        if target - n in s:
            return [nums.index(n), nums.index(target - n)]


def bruteforce(nums, target):
    for i, n1 in enumerate(nums):
        for j, n2 in enumerate(nums[i + 1:], i + 1):
            if n1 + n2 == target:
                return [i, j]


def test_twoSum():
    testcases = [
        ([2,7,11,15], 9, [0,1]),
        ([3,2,4], 6, [1,2]),
        ([3,3], 6, [0,1]),
    ]
    expr = lambda args: Solution().twoSum(*args)
    repr = lambda args: f"twoSum({', '.join(map(str, list(args)))})"
    for *input, result in testcases[:]:
        # assert expr(input) == result
        print(f'{repr(input)} = {expr(input)}')

test_twoSum()