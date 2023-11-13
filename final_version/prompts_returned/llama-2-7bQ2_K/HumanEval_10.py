

def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    """
    if not string:
        return ''
    # 0. Add all suffixes of supplied string to candidate list.
    suffix_list = list(string)
    while len(suffix_list) > 1:
        prefix, suffix = pop_first_two_elements(suffix_list)
        if is_palindrome(prefix):
            yield ''.join((prefix, suffix))
    # 1. Find the longest palindromic string in suffixes of supplied string.
    if len(suffix_list) >= 2:
        max_len = min([len(s) for s in suffix_list])
        for suffix in suffix_list[:-1]:
            yield ''.join((max_len - len(suffix), suffix))
    # 2. Add to candidate list all prefixes of supplied string that are palindromic.
    while not isempty(candidate_list):
        prefix = pop_first_element(candidate_list)
        if is_palindrome(prefix) and len(suffix_list) == 0:
            yield prefix
    raise ValueError('no palindromic string')
