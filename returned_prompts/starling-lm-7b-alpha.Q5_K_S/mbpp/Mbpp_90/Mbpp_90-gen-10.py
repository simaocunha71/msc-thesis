"""
def len_log(s):
    return max([len(i) for i in s])

print(len_log(["python","PHP","bigdata"]))
"""

# Python3 program to find the length of the longest word

# Function to find the length of the longest word
def len_log(s):
    return max(map(len, s))

# Driver code
if __name__ == "__main__":
    s = ["python","PHP","bigdata"]
    print(len_log(s))







"""
The above code is incorrect because when we use the map function in Python, it applies the function to every item of iterable (which is a list) and returns a list of the results. But in the above code, we are not converting the list of results to a single item.

To convert the map object into a single item, we can use the list function in Python. We can modify the code as follows:

def len_log(s):
    return max(list(map(len, s)))

Now, the function will return the length of the longest word in the list.
"""


```
```

```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
``