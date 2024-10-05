The given function `IsEqualToSumEven` should return `true` if the given number `n` can be written as the sum of exactly 4 positive even numbers, and `false` otherwise.

Here is a possible implementation of this function in Go:
```go
func IsEqualToSumEven(n int) bool {
    for i := 2; i <= n/2; i += 2 {
        for j := i; j <= n/2; j += 2 {
            for k := j; k <= n/2; k += 2 {
                for l := k; l <= n/2; l += 2 {
                    if i+j+k+l == n {
                        return true
                    }
                }
            }
        }
    }
    return false
}
```
This function uses four nested loops to iterate over all possible combinations of four positive even numbers that sum up to `n`. If it finds such a combination, it returns `true`. If it doesn't find any, it returns `false`. Note that the outer loop starts from 2 and increments by 2, as we only need to consider positive even numbers. The inner loops also start from the current value of the outer loop and increment by 2, to ensure that each number is considered only once.

For example, if we call `IsEqualToSumEven(8)`, the function will return `true` because 2+2+2+2 equals 8. If we call `IsEqualToSumEven(4)`, the function will return `false` because there is no combination of four positive even numbers that sums up to 4. Similarly, if we call `IsEqualToSumEven(6)`, the function will also return `false`.