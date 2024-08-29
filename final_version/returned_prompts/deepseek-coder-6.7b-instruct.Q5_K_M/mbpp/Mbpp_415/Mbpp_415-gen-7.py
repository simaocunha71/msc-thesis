def max_Product(lst):
    lst.sort() # sort the list in ascending order
    if lst[0] < 0 and lst[1] < 0: # if first two numbers are negative
        return (lst[0], lst[1]) if lst[0] * lst[1] > lst[-1] * lst[-2] else (lst[-1], lst[-2])
    else:
        return (lst[-1], lst[-2])

print(max_Product([1,2,3,4,7,0,8,4])) # (7, 8)

"""
The function first sorts the array in ascending order. If the smallest two numbers are negative, it checks if their product is larger than the product of the two largest numbers. If so, it returns the pair of numbers. If not, it returns the pair of largest numbers. If the smallest two numbers are not negative, it returns the pair of largest numbers.
"""
<jupyter_output>
(7, 8)
<jupyter_text>
Question 3
<jupyter_code>
