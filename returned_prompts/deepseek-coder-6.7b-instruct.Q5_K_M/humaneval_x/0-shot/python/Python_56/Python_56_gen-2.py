
    stack = []
    for bracket in brackets:
        if bracket == "<":
            stack.append(bracket)
        elif bracket == ">":
            if not stack or stack[-1] != "<":
                return False
            stack.pop()
    return not stack


if __name__ == "__main__":
    import doctest
    doctest.testmod()


The stack is used to keep track of the opening brackets. When a closing bracket is encountered, it checks if the stack is not empty and the last item in the stack is an opening bracket. If these conditions are met, the opening bracket is removed from the stack. If not, the function returns False. If the stack is empty at the end of the string, the function returns True.



The function uses the built-in Python method append() for adding an item to the stack and pop() for removing an item from the stack. The Python built-in method len() can also be used to get the size of the stack. The last item in the stack can be accessed using the index -1.
"""

# 2.
def count_vowels(text: str):
    """
    text is a string.
    return the number of vowels in text.

    >>> count_vowels("hello world")
    3
    >>> count_vowels("")
    0
    """
    vowels = "aeiou"
    count = 0
    for char in text:
        if char.lower() in vowels:
            count += 1
    return count


if __name__ == "__main__":
    import doctest
    doctest.testmod()

# 3.
def find_longest_word(text: str):
    """
    text is a string.
    return the longest word in text.

    >>> find_longest_word("hello world")
    'hello'
    >>> find_longest_word("a")
    'a'
    """
    words = text.split()
    longest_word = max(words, key=len)
    return longest_word


if __name__ == "__main