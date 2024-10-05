
def exchange(lst1, lst2):
    """
    :param lst1: List[int]
    :param lst2: List[int]
    :return: str
    """
    lst1_evens = [num for num in lst1 if num % 2 == 0]
    lst2_evens = [num for num in lst2 if num % 2 == 0]
    return "YES" if len(lst1_evens) == len(lst1) and len(lst2_evens) == len(lst2) else "NO"
