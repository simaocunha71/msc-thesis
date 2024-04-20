"""
Write a function to find the nth number in the newman conway sequence.
assert sequence(10) == 6
"""
import math

def sequence(n):
    def fib(stop, start=None):
        if (start is None): #start not specified, so this will be the first element
            return int(math.log10(start)) + math.log10(start - 1)
        
        elif stop < len(fibs):
            return fib(stop-1, start + int(fib(stop)))
        else:
            return int(str(len(fibs))[::-1]) #take the last element of seq and flip it
    return fib(n)
