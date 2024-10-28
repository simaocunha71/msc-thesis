
def pancake_sort(lst: list) -> list:
    """
    Sorts a list using the pancake sort algorithm
    """
    lst = lst[:]
    for i in range(len(lst)-1, 0, -1):
        print(f'i = {i}')
        m = lst.index(max(lst[:i+1]))
        if m != i:
            lst[i], lst[m] = lst[m], lst[i]
            print(f'swap lst[i] ({lst[i]}) with lst[m] ({lst[m]})')
            print(f'lst = {lst}')
        else:
            print(f'lst[i] ({lst[i]}) already max')
    return lst


