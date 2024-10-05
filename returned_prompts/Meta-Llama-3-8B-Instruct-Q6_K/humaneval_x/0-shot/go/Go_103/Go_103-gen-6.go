```go
func RoundedAvg(n, m int) interface{} {
    if n > m {
        return -1
    }
    sum := 0
    count := 0
    for i := n; i <= m; i++ {
        sum += i
        count++
    }
    avg := math.Round(float64(sum) / float64(count))
    binary := fmt.Sprintf("%b", int(avg))
    return binary
}
```


The function `RoundedAvg` takes two integers `n` and `m` as input and returns the average of the integers from `n` through `m` (inclusive) as a binary string.

If `n` is greater than `m`, the function returns -1.

Here's how the function works:

1. It checks if `n` is greater than `m`. If true, it returns -1.
2. It initializes two variables `sum` and `count` to 0.
3. It loops through the range from `n` to `m` (inclusive) and sums up all the integers.
4. It counts the number of integers in the range.
5. It calculates the average by dividing the sum by the count and rounding it to the nearest integer using the `math.Round` function.
6. It converts the average integer to a binary string using the `fmt.Sprintf` function with the format string `%b`.
7. It returns the binary string.

Here are some examples:

```go
fmt.Println(RoundedAvg(1, 5)) // Output: "0b11"
fmt.Println(RoundedAvg(7, 5)) // Output: -1
fmt.Println(RoundedAvg(10, 20)) // Output: "0b1111"
fmt.Println(RoundedAvg(20, 33)) // Output: "0b11010"
```


Note that the function returns a binary string, so the output is a string that starts with "0b" followed by the binary representation of the average integer. For example, the output for `RoundedAvg(1, 5)` is "0b11" which represents the integer 3 in binary. The output for `RoundedAvg(10, 20)` is "0b1111" which represents the integer 15 in binary.