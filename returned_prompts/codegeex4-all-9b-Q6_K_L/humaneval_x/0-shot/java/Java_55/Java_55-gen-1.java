def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

print(fib(10)) # Output: 55
print(fib(1)) # Output: 1
print(fib(8)) # Output: 21
