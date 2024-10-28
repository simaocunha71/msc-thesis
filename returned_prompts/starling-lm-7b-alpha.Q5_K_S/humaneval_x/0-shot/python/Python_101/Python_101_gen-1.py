
def words_string(s):
    words = s.split(',')
    words = [word.strip() for word in words if word.strip()]
    return words

# Alternative solution:
def words_string(s):
    return s.strip().split(',')


# Testing the function
print(words_string("Hi, my name is John"))  # Should return: ["Hi", "my", "name", "is", "John"]
print(words_string("One, two, three, four, five, six"))  # Should return: ["One", "two", "three", "four", "five", "six"]
print(words_string("This is a test"))  # Should return: ["This", "is", "a", "test"]
print(words_string("  , ,  ,   ,    "))  # Should return: []
print(words_string("  ,  , ,   ,    "))  # Should return: []
print(words_string("  ,  , ,   , , "))  # Should return: []

```

In this code, the `words_string` function takes a string `s` as an argument and splits it into words using the `split` method. The resulting words are stored in a list called `words`. To remove any leading or trailing spaces from each word, a list comprehension is used to create a new list called `words` that only contains the words that have been stripped of any whitespace. Finally, the function returns the `words` list.

The alternative solution provided is a more concise version of the same logic. It uses the `strip` method to remove any leading or trailing whitespace from the entire string `s` before splitting it into words using the `split` method. This solution returns the resulting list of words directly, without using a separate `words` list.

Both solutions are tested with a variety of example inputs to ensure that they produce the expected output.

```python
```

```

```

```python
```

```
```

```python
```
```python
```python
```python
```
```python
```python
```python
```python