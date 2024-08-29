def remove_length(s, k):
    words = s.split(" ")
    words = [word for word in words if len(word) != k]
    return " ".join(words)

# Test the function
print(remove_length('The person is most value tet', 3))
<jupyter_output>
person is most value
<jupyter_text>
Question 2
<jupyter_code>
