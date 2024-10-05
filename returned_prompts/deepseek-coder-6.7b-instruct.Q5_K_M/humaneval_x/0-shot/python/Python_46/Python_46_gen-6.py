
def fib4(n: int) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0

    fib = [0, 0, 2, 0]
    for i in range(4, n+1):
        fib.append(fib[i-1] + fib[i-2] + fib[i-3] + fib[i-4])
    return fib[n]


print(fib4(5))
print(fib4(6))
print(fib4(7))
"""
Output:
4
8
14
"""

The function works by using a list to store the computed Fib4 values. For each new value, it adds the previous four values together. This approach eliminates the recursive calls, and makes the function more efficient by reducing the time complexity from exponential to linear.
"""

# In[ ]:



# In[ ]:



# In[ ]:



# In[ ]:



# In[ ]:



# In[ ]:



# In[ ]:



# In[ ]:



# In[ ]:



# In[ ]:



# In[ ]:



# In[ ]:



# In[ ]:



# In[ ]:



# In[ ]:



# In[ ]:



# In[ ]:



# In[ ]:



# In[ ]:



# In[ ]:



# In[ ]:



# In[ ]:



# In[ ]:



# In[ ]:



# In[ ]:



# In[ ]:



# In[ ]:



# In[ ]:



# In[ ]:



# In[ ]:



# In[ ]:

