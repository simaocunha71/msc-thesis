"""
To solve this problem you can use the built-in filter function in Python. The filter function applies a function to every item in an iterable and returns only the items for which the function returns true. You can use a lambda function as the filter function to check if a number is odd or not. Here's how you can define the function:

def filter_oddnumbers(numbers):
    return filter(lambda number: number % 2 == 1, numbers)

Then you can use the function like this:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_numbers = filter_oddnumbers(numbers)
print(list(filtered_numbers))  # Prints: [1, 3, 5, 7, 9]
"""

def filter_oddnumbers(numbers):
    return list(filter(lambda number: number % 2 == 1, numbers))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
assert filter_oddnumbers(numbers)==[1,3,5,7,9]
print("All unit tests passed")






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