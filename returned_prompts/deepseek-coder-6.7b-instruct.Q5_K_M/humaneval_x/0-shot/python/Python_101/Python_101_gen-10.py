
def words_string(s):
    return s.replace(",", " ").split()

# Test cases
print(words_string("Hi, my name is John"))
print(words_string("One, two, three, four, five, six"))

# Expected output:
# ["Hi", "my", "name", "is", "John"]
# ["One", "two", "three", "four", "five", "six"]
<jupyter_output>
['Hi', 'my', 'name', 'is', 'John']
['One', 'two', 'three', 'four', 'five', 'six']
<jupyter_text>
Question 2: Create a function that takes an integer and returns a string with the number in expanded form. For example, given the integer 12, the function should return "One Thousand Two Hundred".
<jupyter_code>
