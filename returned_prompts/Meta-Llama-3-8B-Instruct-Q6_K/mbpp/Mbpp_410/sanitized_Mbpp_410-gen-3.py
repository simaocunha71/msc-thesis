def min_val(lst):
    return min(i for i in lst if isinstance(i, (int, float)))
    #or return min([i for i in lst if isinstance(i, (int, float))]) if you are using python 3.5 or lower
    #or return min(map(lambda x: x if isinstance(x, (int, float)) else float('inf'), lst))
    #or return min((i for i in lst if isinstance(i, (int, float))))
    #or return min(lst)[0] if lst else None
    #or return min(i for i in set(lst) if isinstance(i, (int, float)))
    #or return min(i for i in set(filter(lambda x: isinstance(x, (int, float)), lst))) # python 3.5 or lower
    #or return min(map(lambda x: x if isinstance(x, (int, float)) else float('inf'), filter(lambda x: isinstance(x, (int, float)), lst)))
    #or return min(i for i in set(map(lambda x: x if isinstance(x, (int, float)) else float('inf'), lst))) # python 3.5 or lower
    #or return min(map(lambda x: x if isinstance(x, (int, float)) else float('inf'), set(map(lambda x: x if isinstance(x, (int, float)) else float('inf'), lst)))) # python 3.5 or lower
    #or return min(map(lambda x: x if isinstance(x, (int, float)) else float('inf'), map(lambda x: x if isinstance(x, (int, float)) else float('inf'), lst))) # python 3.5 or lower
    #or return min(map(lambda x: x if isinstance(x, (int, float)) else float('inf'), map(lambda x: x if isinstance(x, (int, float)) else float('inf'), map(lambda x: x if isinstance(x, (int, float)) else float('inf'), lst)))) # python 3.5 or lower
    #or return min(map(lambda x: x if isinstance(x, (int, float)) else float('inf'), map(lambda x: x if isinstance(x, (int, float)) else float('inf'), map(lambda x: x if isinstance(x, (int, float)) else float('inf'), map(lambda x: x if isinstance(x, (int, float)) else float('inf'), lst))))