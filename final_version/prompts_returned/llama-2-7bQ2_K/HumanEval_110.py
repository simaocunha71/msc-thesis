
def exchange(lst1, lst2):
    """In this problem, you will implement a function that takes two lists of numbers,
    and determines whether it is possible to perform an exchange of elements
    between them to make lst1 a list of only even numbers.
    There is no limit on the number of exchanged elements between lst1 and lst2.
    If it is possible to exchange elements between the lst1 and lst2 to make
    all the elements of lst1 to be even, return "YES".
    Otherwise, return "NO".
    For example:
    exchange([1, 2, 3, 4], [1, 2, 3, 4]) => "YES"
    exchange([1, 2, 3, 4], [1, 5, 3, 4]) => "NO"
    It is assumed that the input lists will be non-empty.
    """

    lst1 = sorted(lst1)
    lst2 = sorted(lst2)
    
    
    if len(lst1) <= len(lst2):
        return ""

    even_size = 0
    odd_size = 0
    even_count = 0
    for index, num in enumerate(lst2, start=1):
            if num % 2 == 0:
                even_count += 1
            elif index <= len(lst1) - 1:
                pass
            else:
                odd_count += 1

    for i in range(len(even_count)):
        lst1.pop()
    return "YES" if even_size == 0 and odd_size == 0 else "NO"
