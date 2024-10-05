```go
func IsEqualToSumEven(n int) bool {
    for i := 2; i < n; i += 2 {
        for j := 2; j < n; j += 2 {
            for k := 2; k < n; k += 2 {
                for l := 2; l < n; l += 2 {
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
The code checks all possible combinations of 4 positive even numbers to see if their sum equals the given number `n`. If it finds a combination that sums up to `n`, it returns `true`. If it doesn't find any such combination after checking all possibilities, it returns `false`. This code has a time complexity of O(n^4) due to the four nested loops, which can be inefficient for large values of `n`. 

This code can be optimized by using a more efficient algorithm or by reducing the number of iterations. For example, we can sort the numbers and check if their sum equals `n`. But this will still have a time complexity of O(n^3) which is not efficient for large values of `n`. 

A more efficient solution would be to use a dynamic programming approach to solve this problem. 

Here is a more efficient solution in Go:

```go
func IsEqualToSumEven(n int) bool {
    for i := 2; i < n; i += 2 {
        for j := 2; j < n; j += 2 {
            for k := 2; k < n; k += 2 {
                if i+j+k > n {
                    break
                }
                if i+j+k == n {
                    return true
                }
            }
        }
    }
    return false
}
```
This code still has a time complexity of O(n^3) but it's more efficient than the original code because it breaks out of the inner loop as soon as it determines that the sum of `i`, `j`, and `k` will be greater than `n`. This reduces the number of iterations and makes the code more efficient. 

However, for large values of `n`, this code is still not efficient enough. A more efficient solution would be to use a dynamic programming approach to solve this problem. 

Here is a more efficient solution in Go:

```go
func IsEqualToSumEven(n int)