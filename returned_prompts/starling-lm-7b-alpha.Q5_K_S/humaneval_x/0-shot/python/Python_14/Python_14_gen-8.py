    return [suffixes[i] for i in range(len(string) + 1)]


def all_suffixes(string: str) -> List[str]:
    """ Return list of all suffixes from shortest to longest of the input string
    >>> all_suffixes('abc')
    ['c', 'bc', 'abc']
    """
    return [suffixes[i] for i in range(len(string) + 1)]


def all_permutations(string: str) -> List[str]:
    """ Return a list of all permutations of the input string
    >>> all_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    """

    if len(string) == 1:
        return [string]
    else:
        rest_perms = all_permutations(string[1:])
        first_char = string[0]
        return [first_char + p for p in rest_perms]


def all_anagrams(string: str) -> List[str]:
    """ Return a list of all anagrams of the input string
    >>> all_anagrams('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    """
    if len(string) == 1:
        return [string]
    else:
        char = string[0]
        rest_anagrams = all_anagrams(string[1:])
        rest_anagrams_with_char = [char + anagram for anagram in rest_anagrams]
        rest_anagrams_without_char = [anagram for anagram in rest_anagrams if char not in anagram]
        return rest_anagrams_with_char + rest_anagrams_without_char































































