class Solution:
    def grayCode(self, n: int) -> list[int]:
        gc = [0]
        for exponent in range(n):
            mask = 1 << exponent
            gc += [x ^ mask for x in reversed(gc)]
        return gc

def test_greyCode():
    from pprint import pprint
    testcases = [
        (2, [0, 1, 3, 2]),
        (1, [0, 1]),
        (5, [0,1,3,2,6,7,5,4,12,13,15,14,10,11,9,8,24,25,27,26,30,31,29,28,20,
             21,23,22,18,19,17,16]),
    ]
    for input, result in testcases:
        print(f'grayCode({input}) = {Solution().grayCode(input)}')
        pprint([f'{x:>0{input}b}' for x in Solution().grayCode(input)])
        assert Solution().grayCode(input) == result

test_greyCode()