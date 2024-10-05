    if not strings:
        return None
    longest_string = strings[0]
    for string in strings:
        if len(string) > len(longest_string):
            longest_string = string
    return longest_string


from typing import Dict, List, Optional


def most_frequent(words: List[str]) -> Dict[str, int]:
    """ Return a dictionary of words and the number of times they appear in the list.
    >>> most_frequent([])
    {}
    >>> most_frequent(['a', 'b', 'a', 'c', 'b', 'a'])
    {'a': 3, 'b': 2, 'c': 1}
    """
    counter = {}
    for word in words:
        if word in counter:
            counter[word] += 1
        else:
            counter[word] = 1
    return counter


def remove_duplicates(nums: List[int]) -> List[int]:
    """ Remove all duplicates from a list of numbers, maintaining original order. Return the list.
    >>> remove_duplicates([])
    []
    >>> remove_duplicates([1, 2, 3, 1, 2, 3, 4, 5])
    [1, 2, 3, 4, 5]
    """
    unique_nums = []
    for num in nums:
        if num not in unique_nums:
            unique_nums.append(num)
    return unique_nums


def count_occurrences(nums: List[int], target: int) -> Dict[int, int]:
    """ Return a dictionary mapping each number in nums to the number of times it occurs.
    >>> count_occurrences([1, 2, 3, 2, 3], 2)
    {1: 1, 2: 2, 3: 2}
    >>> count_occurrences([1, 2, 3], 2)
    {1: 1, 2: 1, 3: 1}
    >>> count