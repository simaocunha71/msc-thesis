```
def digit_distance_nums(a, b):
    return sum(abs(int(digit1) - int(digit2)) for pair in zip(str(a), str(b)) for digit1, digit2 in [pair])
```  
Explanation:
The function takes two integers as input, converts them to strings, and then uses the zip function to pair up the digits from the two strings. It then calculates the absolute difference between each pair of digits, and finally sums up these differences. This gives the total sum of the per-digit difference between the two integers. For example, for the input 1 and 2, the function will calculate the difference between 1 and 2, which is 1, and return this value. The unit test `assert digit_distance_nums(1,2) == 1` ensures that the function is working correctly. 





