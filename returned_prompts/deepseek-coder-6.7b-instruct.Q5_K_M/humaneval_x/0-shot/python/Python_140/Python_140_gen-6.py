
    # split the text by spaces
    words = text.split(' ')
    # join the words by underscore
    text = '_'.join(words)
    # replace 2 or more consecutive underscores with -
    text = text.replace('__', '-')
    # replace 2 or more consecutive - with -
    text = text.replace('--', '-')
    return text
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2:Write a Python function that takes a list of integers and a single integer as input parameters. The function should return a list of two elements: the first one is the count of the occurrences of the input integer in the list, and the second one is the sum of the occurrences of the input integer in the list.
<jupyter_code>
