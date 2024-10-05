from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [i if idx == len(numbers) else i for idx, i in enumerate([*numbers, delimeter][:-1])]

print(intersperse([], 4))
print(intersperse([1, 2, 3], 4))


A: 
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num if idx == len(numbers)-1 else num + [delimeter] for idx, num in enumerate(numbers)]

print(intersperse([], 4))
print(in