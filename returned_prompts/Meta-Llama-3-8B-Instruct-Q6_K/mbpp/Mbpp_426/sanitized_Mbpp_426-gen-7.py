def filter_oddnumbers(lst):
    return [num for num in lst if num % 2 != 0]
    # or
    # return list(filter(lambda x: x % 2 != 0, lst)) 
    # or
    # return [x for x in lst if isinstance(x, int) and x % 2 != 0] # if you want to filter only integers
    # or
    # return [x for x in lst if not isinstance(x, int) or x % 2 != 0] # if you want to filter everything except integers
    # or
    # return list(map(lambda x: x if x % 2 != 0 else None, lst))  # if you want to return None for even numbers
    # or
    # return list(filter(lambda x: x % 2 != 0, map(lambda x: x if isinstance(x, int) else None, lst)))  # if you want to filter everything except integers and return None for even numbers
    # or
    # return list(filter(lambda x: isinstance(x, int) and x % 2 != 0, lst))  # if you want to filter only integers
    # or
    # return list(map(lambda x: x if x % 2 != 0 else None, filter(lambda x: isinstance(x, int), lst)))  # if you want to filter everything except integers and return None for even numbers
    # or
    # return list(map(lambda x: x if isinstance(x, int) and x % 2 != 0 else None, lst))  # if you want to filter everything except integers and return None for even numbers
    # or
    # return list(map(lambda x: x if x % 2 != 0 else None, filter(lambda x: isinstance(x, int), lst)))  # if you want to filter everything except integers and return None for even numbers
    # or
    # return list(map(lambda x: x if isinstance(x, int) and x % 2 != 0 else None, filter(lambda x: isinstance(x, int), lst)))  # if you want to filter everything except integers and return None for even numbers
    # or
    # return list(map(lambda x: x if x % 2 != 0 else None, filter(lambda x: isinstance(x, int), lst)))  # if you want to filter everything except integers and return None for even