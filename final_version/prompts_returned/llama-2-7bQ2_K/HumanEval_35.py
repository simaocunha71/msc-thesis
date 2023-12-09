

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    if len(l) == 0:
        return None
    else:
        return l[l.index(max(l))]

def binary_search(l: list, x):
    """Binary Search of an element in a list."""
    low = 0
    high = len(l) - 1
    
    while low <= high:
        mid = (low + high)/2
        
        if l[mid] == x:
            return mid
        elif l[mid] < x:
            high = mid-1
        else:
            low = mid+1
    print("Element not found. Please check the input.")
    
def fibonacci(n):
    """Recursive implementation of Fibonacci sequence."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
nums = [fibonacci(i) for i in range(1,15)]
print("Fibonnaci sequence (Python):", nums[::-1])
