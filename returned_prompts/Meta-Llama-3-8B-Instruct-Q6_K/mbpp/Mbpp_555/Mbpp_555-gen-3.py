```
def difference(n):
    sum_of_cubes = sum(i**3 for i in range(1, n+1))
    sum_of_numbers = (n*(n+1))//2
    return sum_of_cubes - sum_of_numbers
```


Explanation:
The problem is asking to find the difference between the sum of cubes of the first n natural numbers and the sum of the first n natural numbers. 

The sum of the first n natural numbers can be calculated using the formula `n*(n+1)/2`. 

The sum of cubes of the first n natural numbers can be calculated by summing `i**3` for `i` from 1 to `n`. 

The function `difference(n)` calculates these two sums and returns their difference. 

The unit test `assert difference(3) == 30` helps to verify that the function is working correctly. 

For example, `difference(3)` should return `30` because the sum of cubes of the first 3 natural numbers is `1**3 + 2**3 + 3**3 = 1 + 8 + 27 = 36`, and the sum of the first 3 natural numbers is `1 + 2 + 3 = 6`. The difference between these two sums is `36 - 6 = 30`. 