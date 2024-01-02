

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    
    def is_divisible(x): return x%3 == 0
    
    def sort(l: list) -> List[int]:
        l = filter(lambda x: not is_divisible(x), l)
        if len(l) == 1:
            print('Empty')
            raise EmptyError()
            
        return sorted(l, key=lambda x: (not is_divisible(x), int(x)))
    
    def merge(l: list[int], l2: list[int]) -> List[int]:
        return [item for item in zip(*sorted([sort(l), sort(l2)])[1:])] 
    
    return merge(l, sort_third(merge(l, sort_third(l))))