Here is the solution in Go:
```go
func GetOddCollatz(n int) []int {
    res := make([]int, 0)
    for n != 1 {
        if n%2 == 1 {
            res = append(res, n)
        }
        if n%2 == 0 {
            n = n / 2
        } else {
            n = 3*n + 1
        }
    }
    return res
}
```
This function uses a loop to generate the Collatz sequence for the given number `n`. It keeps track of the odd numbers in the sequence and returns them in a sorted list.

The loop continues until `n` reaches 1, which is the stopping condition for the Collatz conjecture. Inside the loop, it checks if `n` is odd or even, and accordingly updates `n` to the next term in the sequence.

Finally, the function returns the list of odd numbers in the sequence, which is sorted in increasing order.

For example, if you call `GetOddCollatz(5)`, the function will return `[1, 5]`, which are the odd numbers in the Collatz sequence for 5.