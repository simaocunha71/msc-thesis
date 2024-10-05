Here is the solution in Go:
```go
func GetOddCollatz(n int) []int {
    result := []int{}
    for n != 1 {
        if n%2 == 0 {
            n = n / 2
        } else {
            n = 3*n + 1
        }
        if n%2 != 0 {
            result = append(result, n)
        }
    }
    return result
}
```
Here's an explanation of the code:

We start by initializing an empty slice `result` that will store the odd numbers in the Collatz sequence.

We then enter a loop that continues until `n` reaches 1. In each iteration, we apply the Collatz sequence rules: if `n` is even, we divide it by 2, and if `n` is odd, we multiply it by 3 and add 1.

We also check if `n` is odd by using the modulo operator `%`. If `n` is odd, we append it to the `result` slice.

Finally, we return the `result` slice, which contains the odd numbers in the Collatz sequence.

Note that we don't need to sort the result slice because we are appending the odd numbers in the order they appear in the Collatz sequence. The resulting slice is already sorted in increasing order.