def remove_length(s, k):
    s = s.split()
    return ' '.join([i for i in s if len(i) != k])

print(remove_length('The person is most value tet', 3))

# Expected Output:
# person is most value

# Time Complexity: O(n)
# Space Complexity: O(n)

"""
This function works by first splitting the input string into a list of words. Then, it creates a new list of words that have a length not equal to k. Finally, it joins this new list of words back into a string and returns it.
"""
<jupyter_output>
person is most value
<jupyter_text>
Question 3:
<jupyter_code>
