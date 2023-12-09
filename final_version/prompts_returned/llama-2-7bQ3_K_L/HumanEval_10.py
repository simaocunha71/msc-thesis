

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
    if string == "":
        return ""
    
    prefix = [1] # [0, 1, ... N-1]

    def append_to_list(prefix: list[int], new_index: int) -> None:
        for i in range(len(prefix), -1, -1):
            if prefix[i]:
                return
            
        prefix.append(new_index)
    
    def find_longest_palindromic_substring_helper(prefix: list[int], start: int, end: int) -> tuple:
        if start > end:
            raise ValueError("start must be less than end")
            
        # Check if we have a match
        if start == end and is_palindrome(string[start:end]):
            return (start, end), True
        
        def find(prefix1: list[int], prefix2: list[int]) -> tuple:
            if len(prefix1) >= 4: # Don't check palindromic prefixes that are shorter than the supplied one.
                return max(find_longest_palindromic_substring_helper((prefix1+len(string)), start, end), (find_longest_palindromic_substring_helper([], start-1, min(start, len(prefix2))), True))[0]
            
            return find_longest_palindromic_substring_helper([],