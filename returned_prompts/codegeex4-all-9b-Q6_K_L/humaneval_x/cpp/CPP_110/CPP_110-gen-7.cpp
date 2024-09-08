def exchange(lst1, lst2):
    """
    >>> exchange([1, 2, 3, 4], [1, 2, 3, 4])
    'YES'
    >>> exchange([1, 2, 3, 4], [1, 5, 3, 4])
    'NO'
    """
    # your code here

C:
def exchange(lst1, lst2):
    """
    >>> exchange([1, 2, 3, 4], [1, 2, 3, 4])
    'YES'
    >>> exchange([1, 2, 3, 4], [1, 5, 3, 4])
    'NO'
    """
    return 'YES' if all(x % 2 == 0 for x in lst1) else 'NO'

