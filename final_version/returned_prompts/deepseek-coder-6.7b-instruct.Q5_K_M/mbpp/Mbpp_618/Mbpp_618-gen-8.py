def div_list(a, b):
    return [x / y for x, y in zip(a, b)]

print(div_list([4,5,6],[1, 2, 3]))

# Output: [4.0, 2.5, 2.0]

# Explanation:
# The function div_list takes in two lists, a and b. It uses the built-in zip function to create a list of pairs from a and b. For each pair, it divides the first number by the second number and adds the result to a new list. This new list is then returned.
<jupyter_output>
<empty_output>
<jupyter_text>
