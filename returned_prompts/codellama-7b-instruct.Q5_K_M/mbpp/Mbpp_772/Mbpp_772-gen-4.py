```
def remove_length(input_string, k):
    words = input_string.split()
    return " ".join([word for word in words if len(word) != k])
```
