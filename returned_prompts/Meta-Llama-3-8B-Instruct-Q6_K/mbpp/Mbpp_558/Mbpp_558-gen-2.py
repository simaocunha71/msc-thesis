```
def digit_distance_nums(a, b):
    return sum(abs(int(digit) - int(digit2)) for digit, digit2 in zip(str(a), str(b)))
```


In this problem, we are asked to find the sum of the per-digit difference between two integers. 

We can solve this problem by converting the integers to strings, then iterate over the characters of the strings and calculate the absolute difference between the characters. Finally, sum up all these differences.

The unit test `assert digit_distance_nums(1,2) == 1` helps us to understand the problem better. It means that the difference between 1 and 2 is 1, and the function should return 1.

The function `digit_distance_nums(a, b)` does exactly that. It converts the integers to strings, then iterate over the characters of the strings using `zip`, calculate the absolute difference between the characters and sum up all these differences using `sum` and `abs`. The result is the sum of the per-digit difference between the two integers. 





The time complexity of this function is O(max(len(a), len(b))), where max(len(a), len(b)) is the maximum number of digits in the two integers. This is because we are iterating over the characters of the strings. The space complexity is O(1), as we are using a constant amount of space to store the sum of the per-digit difference. 