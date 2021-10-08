def precedes(a: str, b: str):
    if len(a) < 1:           return False
    if len(a) != len(b) - 1: return False
    if len(a) == 1:
        if a in b: return True
        else:      return False
    center = len(a) // 2
    if   a[:center] == b[:center]:
        return bool(precedes(a[center:], b[center:]))
    elif a[center:] == b[center + 1:]:
        return bool(precedes(a[:center], b[:center + 1]))
    else:
        return False

def test_precedes():
    testcases = [
        ('abc',    'abac',    True),
        ('abc',    'abcd',    True),
        ('abc',    'zabc',    True),
        ('cba',    'bcad',    False),
        ('a',      'aa',      True),
        ('a',      'aaa',     False),
        ('aa',     'a',       False),
        ('a',      'a',       False),
        ('cdefgh', 'cdefgxh', True),
    ]
    for a, b, result in testcases:
        print(f'{a} precedes {b} {precedes(a, b)} = {result}')
        # assert precedes(a, b) == result


def longestStrChain(words: list[str]) -> int:
    relationships = {}
    cache = {}

    def link(word: str):
        nonlocal relationships, cache
        if word not in relationships: return 1
        if word in cache: return cache[word]
        chain_len = max([link(next) for next in relationships[word]] or [0]) + 1
        cache[word] = chain_len
        return chain_len

    grouped_words = {}
    for word in words:
        grouped_words.setdefault(len(word), [])
        grouped_words[len(word)].append(word)
    for word in words: 
        for next in grouped_words.get(len(word) + 1, []):
            if precedes(word, next):
                relationships.setdefault(word, [])
                relationships[word].append(next)
    for word in relationships: link(word)

    return max(cache.values() or [1])


words = ["a","b","ba","bca","bda","bdca"]   # returns 4
# test_precedes()
longestStrChain(words)
