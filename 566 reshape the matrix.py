from itertools import islice
class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        m, n = len(mat), len(mat[0])
        if m * n != r * c: return mat
        it_elements = (elem for row in mat for elem in row)
        return [[e for e in islice(it_elements, c)] for _ in range(r)]

