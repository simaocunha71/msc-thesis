from collections import Counter

def count_occurance(s):
    return Counter(s).get('std',0)

# count_occurance("letstdlenstdporstd")
# --> 3


# Counter is a dictionary subclass for counting hsashing


"""
The Counter class is a dictionary subclass for counting hsashing. It is a dictionary where the keys are the elements and the values are their counts. 
The Counter class is useful in situations where you want to count the occurrence of elements in a collection. For example, counting the number of times a particular word appears in a text, or counting the frequency of different values in a dataset. 
The Counter class is part of the collections module, which is included in the Python Standard Library, so you don't need to install anything to use it. 

In the given problem, the function count_occurance takes a string as input and uses the Counter class to count the occurrence of the substring 'std' in the string. The Counter class is used to create a dictionary where the keys are all the elements in the string and the values are their counts. The function then uses the get method of the Counter object to retrieve the count of the key 'std' (the substring we are interested in). If the key 'std' is not in the dictionary, the get method returns 0. 

In the given example, the function is called with the string 'letstdlenstdporstd', which contains three occurrences of the substring 'std'. The function returns 3, as expected.
"""

```
from collections import Counter

def count_occurance(s):
    return Counter(s).get('std',0)

# count_occurance("letstdlenstdporstd")
# --> 3
```
```

```


```

```python

```
```

```python

```
```

```python

```
```

```python

```
```
```
```

```python

```
```

```python

```
```

```python

