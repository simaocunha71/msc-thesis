def add_pairwise(t):
    return tuple(t[i] + t[i + 1] for i in range(len(t) - 1))

# Testing the function
print(add_pairwise((1, 5, 7, 8, 10)))  # Expected output: (6, 12, 15, 18)

# Output: (6, 12, 15, 18)
# Which is the correct answer.
<jupyter_output>
(6, 12, 15, 18)
<jupyter_text>
2. Write a Python function to find all the anagrams of a given word from a list of words.
<jupyter_code>
