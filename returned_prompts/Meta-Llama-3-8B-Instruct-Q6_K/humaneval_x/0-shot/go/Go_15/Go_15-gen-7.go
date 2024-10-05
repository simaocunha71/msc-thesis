```go
func StringSequence(n int) string {
    result := ""
    for i := 0; i <= n; i++ {
        result += strconv.Itoa(i) + " "
    }
    return strings.TrimSpace(result)
}
```

Explanation:
This function generates a string sequence of numbers from 0 to `n` inclusive. It uses a for loop to iterate from 0 to `n`, converts each integer to a string using `strconv.Itoa`, appends the string to the `result` variable, and adds a space after each number. Finally, it uses `strings.TrimSpace` to remove the trailing space from the result. The function returns the resulting string.