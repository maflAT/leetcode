class Solution:
    def countVowelPermutation(self, n: int) -> int:
        return permutations(n - 1)

follows = {None: 'aeiou',
            'a': 'e',
            'e': 'ai',
            'i': 'aeou',
            'o': 'iu',
            'u': 'a',}
cache = {}
def permutations(remaining, previous=None):
    cached = cache.get((remaining, previous))
    if cached: return cached
    if remaining == 0: return len(follows[previous])
    result = sum(permutations(remaining - 1, char) for char in follows[previous])
    cache[(remaining, previous)] = result % (10 ** 9 + 7)
    return cache[(remaining, previous)]


def test_countVowelPermutation():
    testcases = [
        (1, 5),
        (2, 10),
        (5, 68),
        (900, 635051351),
    ]
    expr = lambda args: Solution().countVowelPermutation(*args)
    repr = lambda args: f"countVowelPermutation({', '.join(map(str, list(args)))})"
    for *input, result in testcases[:]:
        assert expr(input) == result
        print(f'{repr(input)} = {expr(input)}')

# test_countVowelPermutation()