    prefixes = [s[:i] for i in range(len(s))]
    return prefixes


def all_suffixes(string: str) -> List[str]:
    """ Return a list of all suffixes from shortest to longest of the input string
    >>> all_suffixes('abc')
    ['c', 'bc', 'abc']
    """

    suffixes = [s[-i:] for i in range(len(s))]
    return suffixes

    # O(n) solution using slicing
    # suffixes = []
    # for i in range(len(s)):
    #     suffixes.append(s[i:])
    # return suffixes


def all_permutations(input_list: List[str]) -> List[List[str]]:
    """ Return list of all permutations of the given list
    >>> all_permutations(['a', 'b'])
    [['a', 'b'], ['b', 'a']]
    """

    if len(input_list) == 1:
        return [input_list]

    perms = []
    for elem in input_list:
        rem_list = [x for x in input_list if x != elem]
        for perm in all_permutations(rem_list):
            perms.append([elem] + perm)

    return perms


def all_subsets(input_list: List[str]) -> List[List[str]]:
    """ Return list of all subsets of the given list
    >>> all_subsets(['a', 'b'])
    [['a'], ['b'], ['a', 'b']]
    """

    if len(input_list) == 0:
        return [[]]

    subsets = []
    for elem in input_list:
        rem_list = [x for x in input_list if x != elem]
        for subset in all_subsets(rem_list):
            subsets.append([elem] + subset)

    # Include the empty set at the beginning of the list
    subsets.insert(0, [])
    return subsets

