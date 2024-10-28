```
def frequency(lst, num):
    return lst.count(num)
```


The function takes two parameters, a list and a number. It returns the number of occurrences of the number in the list. The unit test `assert frequency([1,2,3], 4) == 0` ensures that if the number is not in the list, the function returns 0. The built-in `count` method of the list is used to count the occurrences of the number. 
```python
def frequency(lst, num):
    return lst.count(num)
``` 
This function is easy to use and efficient for small lists. However, for large lists, it may be more efficient to use a dictionary to count the occurrences of each number, especially if the list contains many unique numbers. Here is an example of how to do that:
```python
def frequency(lst, num):
    count_dict = {}
    for item in lst:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict.get(num, 0)
```
This function creates a dictionary where the keys are the numbers in the list and the values are the counts of each number. It then returns the count of the given number, or 0 if the number is not in the list. This function is more efficient for large lists, but it is also more complex and may be harder to understand. 
```python
def frequency(lst, num):
    count = 0
    for item in lst:
        if item == num:
            count += 1
    return count
``` 
This function is a simple loop that counts the occurrences of the number in the list. It is easy to understand and use, but it may be less efficient than the previous functions for large lists. 
```python
def frequency(lst, num):
    return sum(1 for item in lst if item == num)
``` 
This function uses a generator expression to count the occurrences of the number in the list. It is easy to understand and use, and it is more efficient than the previous function for large lists. 
```python
def frequency(lst, num):
    return lst.copy().count(num)
``` 
This function creates a copy of the list and then uses the `count` method to count the occurrences of the number in the list. It is easy to understand and use, but it may be less efficient than the previous functions for large lists. 
```