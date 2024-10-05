To solve this problem we can follow these steps:

1. Convert the input string to an array of numbers and names.
2. Sort the array in ascending order.
3. Convert the sorted array back into a string, separated by spaces.

Here's a step-by-step breakdown of how to do this in Python:

1. Split the input string by spaces to create an array of words:
```python
numbers_and_names = numbers.split(' ')
```
2. Initialize an empty list to store the sorted numbers:
```python
sorted_numbers = []
```
3. Iterate through the `numbers_and_names` array and append the numbers to the `sorted_numbers` list:
```python
for word in numbers_and_names:
    if word in ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']:
        sorted_numbers.append(int(word))
```
4. Sort the `sorted_numbers` list in ascending order:
```python
sorted_numbers.sort()
```
5. Convert the sorted `sorted_numbers` list back into a string, separated by spaces:
```python
sorted_string = ' '.join(map(str, sorted_numbers))
```
6. Return the sorted string:
```python
return sorted_string
```

When you put all of this together, the complete solution looks like this:

```python
def sortNumbers(numbers):
    numbers_and_names = numbers.split(' ')
    sorted_numbers = []
    for word in numbers_and_names:
        if word in ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']:
            sorted_numbers.append(int(word))
    sorted_numbers.sort()
    return ' '.join(map(str, sorted_numbers))
```

This function will take a string of numbers and names, sort the numbers from smallest to largest, and return a string with the numbers in the correct