
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    
    evens = []
    for i in xrange(0,len(lst),2):
        if lst[i]%2 == 0:   # If even element is found then add it to the evens list..
            evens.append(lst[i])
        
    return reduce(lambda x,y : x + y,evens)
```
