def max_Product(arr):
    arr.sort()
    return (arr[-1], arr[-2])

print(max_Product([1,2,3,4,7,0,8,4]))

# Another solution using heapq

import heapq

def max_Product(arr):
    heap = heapq.nlargest(2, arr)
    return tuple(heap)

print(max_Product([1,2,3,4,7,0,8,4]))

# Another solution using heapq

import heapq

def max_Product(arr):
    heap = heapq.nlargest(2, arr)
    return tuple(heap)

print(max_Product([1,2,3,4,7,0,8,4]))

# Another solution using sorting

def max_Product(arr):
    arr.sort()
    return (arr[-1], arr[-2])

print(max_Product([1,2,3,4,7,0,8,4]))
<jupyter_output>
(8, 7)
(8, 7)
(8, 7)
(8, 7)
<jupyter_text>
3. Write a Python program to find the sum of all elements in a list using recursion.
<jupyter_code>
def sum_list(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return lst[0] + sum_list(lst[1:])

lst = [1,2,3,4,5]
print(sum_list(lst))
<jupyter_output>
15
<jupyter_text>
4. Write a Python program to calculate the factorial of a number using recursion.
<jupyter_code>
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))
<jupyter_output>
120
<jupyter_