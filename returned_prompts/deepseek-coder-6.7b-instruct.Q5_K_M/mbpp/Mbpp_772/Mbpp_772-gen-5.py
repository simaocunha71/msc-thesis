def remove_length(s, k):
    words = s.split(" ")
    words = [word for word in words if len(word) != k]
    return " ".join(words)

print(remove_length('The person is most value tet', 3))

# Output: 'person is most value'

"""
Explanation:
The function remove_length takes in a string s and an integer k. It splits the string into a list of words using the split() method.
Then it creates a new list of words that have length not equal to k using a list comprehension.
Finally, it joins the words back into a string using the join() method and returns this string.
"""
<jupyter_output>
person is most value
<jupyter_text>
Question 2:
<jupyter_code>
