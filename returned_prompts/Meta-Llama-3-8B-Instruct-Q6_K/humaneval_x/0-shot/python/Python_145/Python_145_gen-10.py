
```
def order_by_points(nums):
    return sorted((num, sum(map(int, str(abs(num))))) for num in nums)
```
This function uses a generator expression to create tuples containing each number and the sum of its digits. The `sorted` function is then used to sort these tuples based on the sum of the digits, and then by the original index in the list if the sums are equal. The result is a list of numbers sorted according to the problem's rules. 

The `abs` function is used to ensure that the sum of the digits is calculated for the absolute value of the number, rather than the number itself. This is because the problem does not specify whether negative numbers should be sorted based on their absolute value or their original value. 

The `map` function is used to convert each character in the string representation of the number to an integer, and then sum these integers to get the sum of the digits.