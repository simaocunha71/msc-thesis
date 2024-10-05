
    for num in l:
        if num >= t:
            return False
    return True

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# The function works by iterating through each number in the list. If it finds a number that is equal to or greater than the threshold, it immediately returns False. If it finishes iterating through the list without finding any such number, it returns True.
<jupyter_output>
<empty_output>
<jupyter_text>
2. Write a function that takes in a list of integers and returns a new list consisting of only the even numbers from the original list.
<jupyter_code>
