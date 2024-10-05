```go
func Solve(N int) string {
    // Convert integer to binary string
    binary := strconv.FormatInt(int64(N), 2)
    
    // Initialize sum variable
    sum := 0
    
    // Iterate through each digit in binary string
    for _, digit := range binary {
        // Convert character to integer and add to sum
        sum += int(digit - '0')
    }
    
    // Convert sum to binary string and return
    return strconv.FormatInt(int64(sum), 2)
}
```