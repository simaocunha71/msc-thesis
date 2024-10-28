```go
func Solve(N int) string {
    binary := strconv.FormatInt(int64(N), 2)
    sum := 0
    for _, digit := range binary {
        digitInt, _ := strconv.Atoi(string(digit))
        sum += digitInt
    }
    return strconv.Itoa(sum)
}
```

Explanation:
1. Convert the integer N to a binary string using strconv.FormatInt.
2. Initialize a variable sum to 0.
3. Iterate through each digit in the binary string.
4. Convert the digit to an integer and add it to the sum.
5. Return the sum as a string using strconv.Itoa.