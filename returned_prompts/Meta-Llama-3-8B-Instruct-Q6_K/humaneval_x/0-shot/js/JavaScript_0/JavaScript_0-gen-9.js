Here is the Python solution:
```
def hasCloseElements(numbers, threshold):
    numbers.sort()
    for i in range(1, len(numbers)):
        if abs(numbers[i] - numbers[i-1]) < threshold:
            return True
    return False
```
Explanation:
This function sorts the list of numbers and then iterates through the list to check if any two consecutive numbers are closer than the given threshold. If it finds such a pair, it returns `True`. If it doesn't find any such pair, it returns `False`.

Here is how you can use it:
```
print(hasCloseElements([1.0, 2.0, 3.0], 0.5))  # Returns False
print(hasCloseElements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # Returns True
```
You can also use this function with a list comprehension:
```
def hasCloseElements(numbers, threshold):
    return any(abs(numbers[i] - numbers[i-1]) < threshold for i in range(1, len(numbers)))
```
This function uses the `any` function to check if any element in the list returned by the generator expression is `True`. The generator expression iterates over the list of numbers and checks if any two consecutive numbers are closer than the given threshold. If it finds such a pair, it returns `True`. If it doesn't find any such pair, it returns `False`.