You can solve this problem in Golang by using a for loop to iterate from 0 to n, and appending each number to a string with a space separator. Here's how you can implement the function StringSequence:

```go
func StringSequence(n int) string {
    result := ""
    for i := 0; i <= n; i++ {
        result += strconv.Itoa(i)
        if i != n {
            result += " "
        }
    }
    return result
}
```

This function converts each number to a string using strconv.Itoa and appends it to the result string. It also adds a space after each number except the last one to meet the requirement of having space-delimited numbers.