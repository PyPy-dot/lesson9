from itertools import combinations


def all_variants(text: str):
    values = []
    for k in range(1, len(text) + 1):
        for t in combinations(text, r=k):
            values.append(''.join(t))
    yield from values


a = all_variants("abc")

for i in a:
    print(i)
