Here is a possible implementation of the `GetOddCollatz` function in Go:
```go
func GetOddCollatz(n int) []int {
    var result []int
    var num int = n
    for num != 1 {
        if num%2 == 1 { // num is odd
            result = append(result, num)
            num = 3*num + 1
        } else { // num is even
            num = num / 2
        }
    }
    result = append(result, 1) // add 1 to the result
    sort.Ints(result)
    return result
}
```
Here's an explanation of how the function works:

1. We initialize an empty slice `result` to store the odd numbers in the Collatz sequence.
2. We set `num` to the input `n`.
3. We loop until `num` reaches 1.
4. Inside the loop, we check if `num` is odd or even.
5. If `num` is odd, we append it to the `result` slice and update `num` to the next value in the Collatz sequence (which is 3 times `num` plus 1).
6. If `num` is even, we update `num` to the next value in the Collatz sequence (which is half of `num`).
7. After the loop, we append 1 to the `result` slice (since 1 is the final value in the Collatz sequence).
8. We sort the `result` slice in increasing order using the `sort.Ints` function.
9. Finally, we return the sorted `result` slice.

You can test the function with different input values, such as `GetOddCollatz(5)`, to see that it returns the correct result.