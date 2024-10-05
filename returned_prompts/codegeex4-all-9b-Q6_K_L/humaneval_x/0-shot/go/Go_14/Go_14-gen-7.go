Here is a solution to your problem using Go:

```go
func AllPrefixes(str string) []string {
    result := make([]string, 0, len(str))
    for i := 1; i <= len(str); i++ {
        result = append(result, str[:i])
    }
    return result
}
```

This solution uses a loop to create all prefixes of the input string. The loop variable `i` is used to specify the length of the prefix. The `[:i]` slice notation is used to create the prefix. The `append` function is used to add the prefix to the result slice.

I hope this helps! Let me know if you have any further questions.