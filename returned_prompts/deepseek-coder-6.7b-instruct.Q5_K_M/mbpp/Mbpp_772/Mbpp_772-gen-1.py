
def remove_length(string, k):
    words = string.split()
    words = [word for word in words if len(word) != k]
    return ' '.join(words)

print(remove_length('The person is most value tet', 3))
<jupyter_output>
person is most value
<jupyter_text>
Q7. Write a function to remove all the occurrences of a specific item from the list.
<jupyter_code>
