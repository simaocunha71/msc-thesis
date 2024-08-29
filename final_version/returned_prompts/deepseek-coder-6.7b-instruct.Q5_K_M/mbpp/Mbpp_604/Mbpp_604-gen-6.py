
def reverse_sentence(s):
    return " ".join(s.split(" ")[::-1])

print(reverse_sentence("python program"))

# This function works by splitting the sentence into a list of words using the split() function and then reversing that list using the [::-1] slice. It then joins the reversed list back into a string with the join() function.

# The output of this program will be:
# program python

# This is because the split() function splits the string at the occurrence of " " (space) and the join() function joins the reversed list with " " (space) as the separator.

# The [::-1] slices the list in reverse order.

# This is a very efficient way of reversing the words in a string.
<jupyter_output>
program python
<jupyter_text>
Question 2:Given a string, you need to reverse every word in the string, but the order of words should remain the same.Input: String contains set of words seperated by spaceOutput: Reverse every word in the string but keep the order of words same.Example:Input: "Hello World"Output: "olleH