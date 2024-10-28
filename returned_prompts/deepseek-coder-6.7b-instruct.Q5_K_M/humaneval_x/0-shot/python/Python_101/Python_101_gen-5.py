
def words_string(s):
    return s.replace(",", " ").split()

print(words_string("Hi, my name is John"))
print(words_string("One, two, three, four, five, six"))

# Output:
# ['Hi', 'my', 'name', 'is', 'John']
# ['One', 'two', 'three', 'four', 'five', 'six']
<jupyter_output>
['Hi', 'my', 'name', 'is', 'John']
['One', 'two', 'three', 'four', 'five', 'six']
<jupyter_text>
Problem 3: Write a Python function to find the factorial of a number. The factorial of a number is the product of all positive integers less than or equal to that number. For example, the factorial of 5 is 5*4*3*2*1.
<jupyter_code>
