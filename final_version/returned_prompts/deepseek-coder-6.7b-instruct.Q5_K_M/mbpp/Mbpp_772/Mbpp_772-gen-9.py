def remove_length(s, k):
    words = s.split()
    result = [word for word in words if len(word) != k]
    return ' '.join(result)

print(remove_length('The person is most value tet', 3))
<jupyter_output>
person is most value
<jupyter_text>
Q2:
<jupyter_code>
