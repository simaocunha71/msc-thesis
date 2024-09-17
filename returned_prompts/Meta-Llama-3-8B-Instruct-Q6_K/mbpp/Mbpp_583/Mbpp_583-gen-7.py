```
def catalan_number(n):
    if n <= 1:
        return 1
    else:
        catalan = [0] * (n+1)
        catalan[0] = catalan[1] = 1
        for i in range(2, n+1):
            for j in range(i):
                catalan[i] += catalan[j] * catalan[i - j - 1]
        return catalan[n]
```    
The function `catalan_number(n)` calculates the `n`th Catalan number using dynamic programming. It initializes a list `catalan` of size `n+1` with all elements set to `0`. It then sets `catalan[0]` and `catalan[1]` to `1`, as the base cases for the recursion. 

Then it iterates over the range `2` to `n`, and for each `i` in this range, it calculates `catalan[i]` as the sum of `catalan[j] * catalan[i - j - 1]` over all `j` in the range `0` to `i`. This is because the `n`th Catalan number is the sum of the product of the `j`th Catalan number and the `(i - j - 1)`th Catalan number over all `j` in the range `0` to `i`.

Finally, it returns `catalan[n]`, which is the `n`th Catalan number. The time complexity of this function is O(n^2), as it involves nested loops over the range `0` to `n`. The space complexity is O(n), as it requires a list of size `n+1` to store the Catalan numbers. 
The unit test `assert catalan_number(10)==16796` ensures that the function returns the correct value for the 10th Catalan number, which is 16796. 

This function can be used to calculate the `n`th Catalan number for any positive integer `n`. It is efficient and accurate, making it suitable for practical applications. 
```python
catalan_number(10)
``` 
This will return `16796`, which is the 10th Catalan number. 
```python
catalan_number(5)
``` 
This will return `42`, which is the 5th Catalan number. 
```python
catalan_number(1)
```