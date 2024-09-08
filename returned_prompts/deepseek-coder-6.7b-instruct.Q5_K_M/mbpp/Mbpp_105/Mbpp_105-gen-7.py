def count(lst):
    count = 0
    for i in lst:
        if i == True:
            count += 1
    return count

print(count([True,False,True])) # Output: 2


# Other solution using list comprehension
def count(lst):
    return sum([1 for i in lst if i == True])

print(count([True,False,True])) # Output: 2

# Another solution using built-in Python function sum()
def count(lst):
    return sum(i == True for i in lst)

print(count([True,False,True])) # Output: 2
<jupyter_output>
2
2
2
<jupyter_text>
Question 4:
<jupyter_code>
