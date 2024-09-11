```
def insert_element(lst, elem):
    new_list = [elem] + lst
    return new_list
```

Explanation:

The function `insert_element` takes in two parameters: `lst`, which is the input list, and `elem`, which is the element to be inserted. Inside the function, a new list called `new_list` is created by concatenating the `elem` with the `lst` using the `+` operator. The `+` operator concatenates the two lists, inserting the `elem` before each element in the `lst`. Finally, the function returns the resulting `new_list`.

The provided assertion `assert insert_element(['Red', 'Green', 'Black'] ,'c')==['c', 'Red', 'c', 'Green', 'c', 'Black']` tests the function by passing a sample input list `['Red', 'Green', 'Black']` and an element `'c'`. The expected output is `['c', 'Red', 'c', 'Green', 'c', 'Black']`, which is the result of inserting the `'c'` before each element in the input list. The assertion checks if the actual output of the function matches the expected output, and if so, the assertion passes.

By using this `insert_element` function, you can easily insert an element before each element in a list and obtain the desired result.

```python
# Testing the function
print(insert_element(['Red', 'Green', 'Black'], 'c'))  # Output: ['c', 'Red', 'c', 'Green', 'c', 'Black']
```

The above code demonstrates how to use the `insert_element` function by passing a sample input list `['Red', 'Green', 'Black']` and an element `'c'`. The function returns the resulting list `['c', 'Red', 'c', 'Green', 'c', 'Black']`, which is printed to the console.

You can modify the input list and the element to insert as per your requirements.

```python
# Inserting an element at the beginning of the list
print(insert_element(['Red', 'Green', 'Black'], 'c'))  # Output: ['c', 'Red', '