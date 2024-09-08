
def remove_odd(numbers):
    return [num for num in numbers if num % 2 == 0]

print(remove_odd([1,2,3]))

# Output: [2]

# The function uses a list comprehension to create a new list that only includes the even numbers from the given list. The condition num % 2 == 0 checks if a number is even.
<jupyter_output>
[2]
<jupyter_text>
Question 2:
<jupyter_code>
