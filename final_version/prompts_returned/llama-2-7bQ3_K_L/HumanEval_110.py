
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

    even_lst = []
    odd_lst = []
    
    print("Inserting elements to the even lst")
    for a in lst1:
        if a % 2 == 0:
            even_lst.append(a)
    print("\nInserting elements to the odd lst")
    for b in lst2:
        if b % 2 == 1:
            odd_lst.append(b)
    # Checking whether possible or not
    if len(even_lst) == len(odd_lst):
        print("Inserting even numbers to the even lst")
        for a in odd_lst:
            even_lst.append(a)
        print("\nInserting odd numbers to the odd lst")
        for b in even_lst:
            odd_lst.append(b)
        
    return "YES" if len(even_lst) == len(odd_lst) else "NO"