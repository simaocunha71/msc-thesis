    num_dict = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }

    return " ".join(sorted(numbers.split(), key=lambda x: num_dict[x]))

I'm trying to solve these problems in python. I'm using python 3.8.2 and I'm following along with a book by Peter Norvig. I have been able to solve the first two problems and understand them perfectly. But I'm having trouble with the third problem.
The error message I'm getting is:
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 5, in separate_paren_groups
TypeError: 'int' object is not iterable

I'm not sure what's going on here.

A: The error is happening because you are trying to iterate over an integer in your for loop in the separate_paren_groups() function.
In your for loop, you are trying to iterate over the 'current_depth' variable which is an integer. That's why you are getting a TypeError saying "'int' object is not iterable".
Here is the line causing the error:
for c in current_depth:

This line should be replaced with:
for c in str(current_depth):

This will convert the integer to a string, which then can be iterated over.

A: The error is due to the fact that the variable 'current_depth' is an integer and you are trying to iterate over it. You can't iterate over an integer, so you need to convert it to a string. Here is the corrected function:
def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list