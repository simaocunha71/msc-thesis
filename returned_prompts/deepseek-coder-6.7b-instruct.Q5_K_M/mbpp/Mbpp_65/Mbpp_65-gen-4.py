
def recursive_list_sum(lst):
    total = 0
    for i in lst:
        if type(i) == list:
            total += recursive_list_sum(i)
        else:
            total += i
    return total

print(recursive_list_sum([1, 2, [3,4],[5,6]])) # Should return 21

# Another way to solve it using list comprehension

def recursive_list_sum(lst):
    return sum(recursive_list_sum(i) if isinstance(i, list) else i for i in lst)

print(recursive_list_sum([1, 2, [3,4],[5,6]])) # Should return 21


# Using built-in sum() and generator expression

def recursive_list_sum(lst):
    return sum(recursive_list_sum(i) if isinstance(i, list) else i for i in lst)

print(recursive_list_sum([1, 2, [3,4],[5,6]])) # Should return 21
<jupyter_output>
21
21
21
<jupyter_text>
Task 2:Write a Python program to find the maximum and minimum value in a given set of data. Your program should accept a list of numbers and return the maximum and minimum values as a tuple.
<jupyter_code>
# 