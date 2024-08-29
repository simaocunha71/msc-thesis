def max_Product(lst):
    lst.sort()
    if lst[0] * lst[1] > lst[-1] * lst[-2]:
        return (lst[0], lst[1])
    else:
        return (lst[-1], lst[-2])

print(max_Product([1,2,3,4,7,0,8,4]))

"""
Explanation:
This function sorts the list in ascending order and then checks whether the product of the smallest two numbers or the largest two numbers is greater. 
The function then returns the pair with the highest product.
"""

#Alternate solution
def max_Product(lst):
    highest = max(lst)
    lst.remove(highest)
    second_highest = max(lst)
    return (highest, second_highest)

print(max_Product([1,2,3,4,7,0,8,4]))

"""
Explanation:
In this alternate solution, we first find the maximum element in the list and then remove it from the list. After that, we find the maximum again which will be the second highest. We then return a tuple of these two numbers.
"""
<jupyter_output>
(7, 8)
(7, 8)
<jupyter_text>
Question 2: Write a Python function that accepts a string and calculates the number of digits, letters and other characters in the string.
<jupyter_code>
def count_characters(s):
    count_digits = 0
    count_letters = 0
    count_others = 0
    
    for i in s:
        if i.isdigit():
            count_digits += 1
        elif i.isalpha():
            count_letters += 1
        else:
            count_others += 1
    return count_digits, count_letters, count_others

print(count_characters('Hello123!'))
<jupyter_output>
(3, 5, 2)
<jupyter_text>
Question 3: Write a Python