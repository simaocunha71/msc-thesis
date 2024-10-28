```
def sort_array(arr):
    return sorted(arr, key=lambda x: (bin(x).count('1'), x))
```


Explanation:
The task is to sort an array of non-negative integers according to the number of ones in their binary representation in ascending order. In case of similar number of ones, sort based on decimal value.

The sorted function in Python is used to sort the array. It takes a function as an argument, known as the key function, which is used to determine the sort order.

The key function in this case is a lambda function that returns a tuple. The first element of the tuple is the count of ones in the binary representation of the number, and the second element is the number itself. This means that the sorting is first done based on the number of ones in the binary representation, and then based on the decimal value.

For example, for the number 5, the binary representation is 101, which has 2 ones. For the number 4, the binary representation is 100, which has 1 one. So, 5 comes after 4 in the sorted array.

The same logic applies to the other numbers in the array. The sorted function then uses this key function to sort the array accordingly.