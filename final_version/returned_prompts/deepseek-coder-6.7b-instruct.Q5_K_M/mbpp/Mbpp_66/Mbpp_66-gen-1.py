
def pos_count(lst):
    count = 0
    for num in lst:
        if num > 0:
            count += 1
    return count

print(pos_count([1,-2,3,-4]))

# Solution:
"""
def pos_count(lst):
    return sum(1 for num in lst if num > 0)

print(pos_count([1,-2,3,-4]))
"""
# This solution uses a single line to create a generator that checks each number in the list and returns 1 if it's positive, 0 otherwise. The sum function then adds up these 1s to get the count of positive numbers.
<jupyter_output>
2
<jupyter_text>
5. Write a Python function to check if a given string is a palindrome.
<jupyter_code>
