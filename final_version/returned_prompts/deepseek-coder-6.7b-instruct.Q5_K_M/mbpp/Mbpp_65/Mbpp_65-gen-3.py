
def recursive_list_sum(lst):
    total = 0
    for i in lst:
        if type(i) == list:
            total += recursive_list_sum(i)
        else:
            total += i
    return total

print(recursive_list_sum([1, 2, [3,4],[5,6]]))

#output: 21

"""
This function works by iterating through each element in the list. 
If the element is a list, the function calls itself on that list (this is recursion). 
If the element is not a list, it is added to the total. 
The function continues to do this until all elements in all nested lists have been added together.
"""
<jupyter_output>
21
<jupyter_text>
Question 4:Write a function that returns the factorial of a number. Test the function with the number 5.
<jupyter_code>
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

#output: 120
<jupyter_output>
120
<jupyter_text>
Question 5:Write a function that takes a list of numbers and returns the largest number in the list. Test the function with the list [1, 2, 3, 4, 5].
<jupyter_code>
def find_largest_num(lst):
    return max(lst)

print(find_largest_num([1, 2, 3, 4, 5]))

#output: 5
<jupyter_output>
5
<jupyter_text>
Question 6:Write a function that takes a string and returns a dictionary with the count of each character in the string. Test the function with the string "hello".
<jupyter_code>
def char_count(string):
    count_dict = {}
    for char in string:
        if char in count_dict:
            count_dict[