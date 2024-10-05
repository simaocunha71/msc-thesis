// Your code here
}  // SumToN


Solution:
```go
func SumToN(n int) int {
    sum := 0
    for i := 1; i <= n; i++ {
        sum += i
    }
    return sum
}
```  // SumToN
```
The function `SumToN` takes an integer `n` as input and returns the sum of all integers from 1 to `n`. The function uses a for loop to iterate from 1 to `n`, adding each integer to a running total `sum`. The function finally returns the total sum. This function is a simple implementation of the formula for the sum of an arithmetic series, which is `n*(n+1)/2`. However, the problem statement asks for a function that sums numbers from 1 to `n`, which is a more straightforward and easy-to-understand approach.