

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """

    return 2 if n % 2 == 0 else n // 2
```

### Explanation: 

We know this problem has the following properties, that we can use to our advantage: 

- The input is always an integer and greater than or equal to one.
- We cannot use numbers with more decimal places than necessary (e.g. 153)

To achieve these requirements, we simply make sure that we only multiply the largest number by a number less than n / 2 (and not 10 ^ k), where k is the number of digits in the input. This also means that we can use the largest number to divide the input by.

### Time Complexity:   
We have two loops, so it will take O(n) time in total:  
O(n) - first loop to find a divisor (where n is at least 2)
O(1) - check if divisors == n // divisor. In our case where divisors is 5, n <= 5 so we check if divisor == n / divisor and this takes O(1)

### Space Complexity:  
Since it's just two lines of code which only contain integers (or variables), the space complexity is O(0).