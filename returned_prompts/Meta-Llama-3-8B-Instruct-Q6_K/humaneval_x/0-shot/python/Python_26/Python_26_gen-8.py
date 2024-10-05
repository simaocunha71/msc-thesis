from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result
# or
def remove_duplicates(numbers: List[int]) -> List[int]:
    return list(dict.fromkeys(numbers))
# or
def remove_duplicates(numbers: List[int]) -> List[int]:
    return list(set([x for x in numbers if numbers.count(x) == 1]))
# or
def remove_duplicates(numbers: List[int]) -> List[int]:
    result = []
    for num in numbers:
        if numbers.count(num) == 1:
            result.append(num)
    return result
# or
from collections import OrderedDict

def remove_duplicates(numbers: List[int]) -> List[int]:
    return list(OrderedDict.fromkeys(numbers))
# or
from collections import defaultdict

def remove_duplicates(numbers: List[int]) -> List[int]:
    counts = defaultdict(int)
    for num in numbers:
        counts[num] += 1
    return [num for num in numbers if counts[num] == 1]
# or
from collections import Counter

def remove_duplicates(numbers: List[int]) -> List[int]:
    counts = Counter(numbers)
    return [num for num in numbers if counts[num] == 1]
# or
from collections import defaultdict

def remove_duplicates(numbers: List[int]) -> List[int]:
    result = []
    counts = defaultdict(int)
    for num in numbers:
        if counts[num] == 0:
            result.append(num)
            counts[num] += 1
    return result
# or
from collections import OrderedDict

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result
# or
from collections import defaultdict

def remove_duplicates(numbers: List[int]) -> List[int]:
    counts = defaultdict(int)
    for num in numbers:
        counts[num] += 1
    return [num for num in numbers if counts[num] == 1]
# or
from collections import OrderedDict

def remove_duplicates(numbers: List[int]) -> List[int]:
    return list(OrderedDict.fromkeys(numbers))
# or
from collections import defaultdict

def remove_duplicates(numbers: List[int]) -> List[int]:
    result = []
    counts