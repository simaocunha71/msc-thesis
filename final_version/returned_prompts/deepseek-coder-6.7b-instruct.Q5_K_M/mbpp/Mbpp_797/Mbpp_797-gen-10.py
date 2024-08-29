def sum_in_range(l,r):
    sum_odd = 0
    for i in range(l, r+1):
        if i % 2 != 0:
            sum_odd += i
    return sum_odd

print(sum_in_range(2,5))

# or using list comprehension
def sum_in_range(l,r):
    return sum([i for i in range(l, r+1) if i % 2 != 0])

print(sum_in_range(2,5))

# or using sum and generator expression
def sum_in_range(l,r):
    return sum((i for i in range(l, r+1) if i % 2 != 0))

print(sum_in_range(2,5))
<jupyter_output>
8
8
8
<jupyter_text>
Write a Python program to find the sum of all even natural numbers within the range l and r.
<jupyter_code>
def sum_in_range(l,r):
    sum_even = 0
    for i in range(l, r+1):
        if i % 2 == 0:
            sum_even += i
    return sum_even

print(sum_in_range(2,5))
<jupyter_output>
6
<jupyter_text>
Write a Python program to find the largest number in a list.
<jupyter_code>
def find_largest(lst):
    return max(lst)

print(find_largest([1,2,3,4,5]))
<jupyter_output>
5
<jupyter_text>
Write a Python program to find the smallest number in a list.
<jupyter_code>
def find_smallest(lst):
    return min(lst)

print(find_smallest([1,2,3,4,5]))
<jupyter_output>
1
<jupyter_text>
Write a Python program to find the second largest number in a list.
<jup