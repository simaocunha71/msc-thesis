def div_list(l1, l2):
    return [a/b for a, b in zip(l1, l2)]

print(div_list([4,5,6],[1, 2, 3]))

# Output: [4.0, 2.5, 2.0]

# Explanation: The function div_list takes two lists l1 and l2 as input. It uses the zip function to pair up corresponding elements from both lists. Then, it uses a list comprehension to divide each pair of elements, and returns the resulting list.
<jupyter_output>
[4.0, 2.5, 2.0]
<jupyter_text>
