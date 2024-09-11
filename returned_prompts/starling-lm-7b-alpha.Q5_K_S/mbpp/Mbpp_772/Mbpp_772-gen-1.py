"""
def remove_length(string, k):
    words = string.split()
    new_words = []
    for word in words:
        if len(word) != k:
            new_words.append(word)
    new_string = " ".join(new_words)
    return new_string

print(remove_length('The person is most value tet', 3))
"""

def remove_length(string, k):
    new_string = ""
    for word in string.split():
        if len(word) != k:
            new_string += word + " "
    return new_string[:-1]

print(remove_length('The person is most value tet', 3))



# Made By Mostafa_Khaled
```