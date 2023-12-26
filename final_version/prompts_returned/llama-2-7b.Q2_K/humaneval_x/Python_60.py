

def sum_to_n(n: int):
    """sum_to_n is a function that sums numbers from 1 to n.
    >>> sum_to_n(30)
    465
    >>> sum_to_n(100)
    5050
    >>> sum_to_n(5)
    15
    >>> sum_to_n(10)
    55
    >>> sum_to_n(1)
    1
    """
    def _sum_to_n(n: int):
        x = []
        for i in range(1, n+1):  # 0 is ignored. It is a special value
            if i % 2 == 1:
                x += [i]
        return sum([j for j in x])  
    return _sum_to_n