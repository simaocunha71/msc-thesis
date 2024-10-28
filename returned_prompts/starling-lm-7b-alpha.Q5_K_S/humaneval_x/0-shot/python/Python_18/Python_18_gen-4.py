
Here's one possible solution to the problem:

```python
def how_many_times(string, substring):
    return len([i for i in range(len(string)) if string[i:i+len(substring)] == substring])
```

This function works by iterating over the indexes of the `string` with a step size equal to the length of the `substring`. For each index `i`, it checks if the `substring` is equal to the substring of `string` starting at index `i`. If the condition is satisfied, it adds the index to a list. After the iteration, the function returns the length of the list, which is the number of times the `substring` can be found in the `string`.

The time complexity of this function is O(n), where `n` is the length of the `string`. This is because the function iterates over the indexes of the `string` once, and for each index it checks a substring of length `len(substring)`.

Here's an example of how to use the function:

```python
print(how_many_times('', 'a'))  # Output: 0
print(how_many_times('aaa', 'a'))  # Output: 3
print(how_many_times('aaaa', 'aa'))  # Output: 3
```

In the first example, the substring `'a'` cannot be found in the empty string, so the function returns 0. In the second example, the substring `'a'` is present three times in the string `'aaa'`, so the function returns 3. In the third example, the substring `'aa'` is present three times in the string `'aaaa'`, so the function returns 3.

```python
```

I hope this helps! Let me know if you have any more questions.

```python

```

```python
```

```python
```

```python
```

```python
```

```python
```

```python
```

```python
```

```python
```

```python
```

``