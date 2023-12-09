

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if not n in (1, 2, 4):
        yield 1
        for i in range(n // 2 + 1):
            # The line above is a simple and fast way to calculate the next fibonacci number.
            yield fib(i + 1)
            if i > 6:
                break
            
def fib_recursive(n: int, memo=None, maxiter=1000):
    """Recursive Function
    
    >>> fib_recursive(8, memo=[], maxiter=250)
    34
    >>> fib_recursive(9, memo=[34], maxiter=250)
    67
    >>> fib_recursive(10, memo=[67],[67])
    138
    """
    if n == 2:
        return 2
    elif n in (1,2):
        return n
    else:
        pre = fib([0], 1)
        
        curr_sum = sum(pre,0)
        memo = [curr_sum] + list(pre[1:])
        
        if curr_sum > maxiter:
            raise ValueError('Maxiter reached!') # If the user gives some really large n's, this will be called.
    
        return fib([0], 1, memo=memo)

if __name__ == '__main__':
    print(fib_recursive(3))