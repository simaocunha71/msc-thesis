from typing import List


def concatenate(strings: List[str]) -> str:
    return ''.join(strings)


print(concatenate([]))  # ''
print(concatenate(['a', 'b', 'c']))  # 'abc'


# 或者更简单的方法：

def concatenate(strings: List[str]) -> str:
    return ''.join(strings)


print(concatenate([]))  # ''
print(concatenate(['a', 'b', 'c']))  # 'abc'


# 或者使用 reduce 函数：

from typing import List
from functools import reduce


def concatenate(strings: List[str]) -> str:
    return reduce((lambda x, y: x + y), strings)


print(concatenate([]))  # ''
print(concatenate(['a', 'b', 'c']))  # 'abc'
"""

# 或者使用 for 循环：

from typing import List


def concatenate(strings: List[str]) -> str:
    result = ""
    for s in strings:
        result += s
    return result


print(concatenate([]))  # ''
print(concatenate(['a', 'b', 'c']))  # 'abc'
"""


# 或者使用 while 循环：

from typing import List


def concatenate(strings: List[str]) -> str:
    result = ""
    i = 0
    while i < len(strings):
        result += strings[i]
        i += 1
    return result


print(concatenate([]))  # ''
print(concatenate(['a', 'b', 'c']))  # 'abc'
"""


# 或者使用递归：

from typing import List


def concatenate(strings: List[str]) -> str:
    if len(strings) == 0:
        return ""
    return strings[0] + concatenate(strings[1:])


print(concatenate([]))  # ''
