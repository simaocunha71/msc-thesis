"""
The problem is to create a function that removes all whitespaces from a string.

Here's a step-by-step explanation of how to solve this problem:

1. Define a function called `remove_all_spaces` that takes a single parameter called `s`. This parameter represents the string from which we want to remove whitespaces.
2. Within the `remove_all_spaces` function, create a variable called `result` and assign it the value of the input string `s`. This is the string from which we want to remove whitespaces.
3. Next, we need to iterate over each character in the string. To do this, we can use a `for` loop that iterates over the length of the string. The loop variable `i` will take on the value of each index in the string.
4. Within the `for` loop, we need to check if the current character at index `i` is a whitespace. We can do this by using the `isspace()` method on the character. This method returns `True` if the character is a whitespace, and `False` otherwise.
5. If the current character is a whitespace, we want to skip over it and move on to the next character. To do this, we can use the `continue` keyword within the `for` loop. The `continue` keyword causes the loop to skip the rest of its body and move on to the next iteration.
6. If the current character is not a whitespace, we want to add it to the `result` string. We can do this by concatenating the character to the `result` string using the `+=` operator.
7. After the `for` loop has finished iterating over all characters in the string, the `result` string will contain all non-whitespace characters from the original string.
8. Finally, we can return the `result` string from the `remove_all_spaces` function.

Here's the complete code for the `remove_all_spaces` function:

def remove_all_spaces(s):
    result = ""
    for i in range(len(s)):
        if s[i].isspace():
            continue
        result += s[i]
    return result

To test the `remove_all_spaces`