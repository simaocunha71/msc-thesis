from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    prefixes = []
    for i in range(1, len(string)+1):
        prefix = string[:i]
        if not prefix:  # no need to check len()
            continue
        prefixes.append(prefix)
    return sorted(prefixes)
