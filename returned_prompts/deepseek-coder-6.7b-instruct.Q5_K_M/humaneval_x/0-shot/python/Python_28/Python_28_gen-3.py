from typing import List


def concatenate(strings: List[str]) -> str:
    return ''.join(strings)


print(concatenate([]))
print(concatenate(['a', 'b', 'c']))

# 