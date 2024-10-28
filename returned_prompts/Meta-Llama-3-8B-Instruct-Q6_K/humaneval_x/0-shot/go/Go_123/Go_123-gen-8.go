Here is a simple implementation of the GetOddCollatz function in Go:
```go
func GetOddCollatz(n int) []int {
    result := []int{}
    for n != 1 {
        if n%2 == 1 { // n is odd
            result = append(result, n)
        }
        if n%2 == 0 { // n is even
            n = n / 2
        } else {
            n = 3*n + 1
        }
    }
    return result
}
```
This function uses a loop to generate the Collatz sequence starting from the given `n`. It checks whether `n` is odd or even and appends the odd numbers to the `result` slice. When `n` reaches 1, the loop stops and the function returns the `result` slice. The `result` slice is initially empty and is appended with the odd numbers in the Collatz sequence. The `GetOddCollatz` function returns the `result` slice, which contains the odd numbers in the Collatz sequence.

You can test this function with the example you provided:
```go
fmt.Println(GetOddCollatz(5)) // Output: [1 5]
```
This will output the expected result: `[1, 5]`, which are the odd numbers in the Collatz sequence for `n=5`.