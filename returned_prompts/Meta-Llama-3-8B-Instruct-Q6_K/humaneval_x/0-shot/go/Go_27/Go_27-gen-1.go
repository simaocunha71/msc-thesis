You can use the built-in `strings.ToUpper()` and `strings.ToLower()` functions in Go to achieve this. Here's the solution:

```go
func FlipCase(str string) string {
    result := ""
    for _, char := range str {
        if strings.ContainsAny(string(char), "abcdefghijklmnopqrstuvwxyz") {
            result += strings.ToUpper(string(char))
        } else {
            result += strings.ToLower(string(char))
        }
    }
    return result
}
```

In this code, we iterate over each character in the input string. If the character is a lowercase letter (checked using `strings.ContainsAny()`), we convert it to uppercase using `strings.ToUpper()`. If the character is an uppercase letter, we convert it to lowercase using `strings.ToLower()`. The result is a new string with the case of each letter flipped. 

You can test this function with the example you provided:

```go
fmt.Println(FlipCase("Hello")) // Output: "hELLO"
``` 