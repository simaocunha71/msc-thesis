```go
func FilterByPrefix(strings []string, prefix string) []string {
    result := make([]string, 0)
    for _, s := range strings {
        if strings.HasPrefix(s, prefix) {
            result = append(result, s)
        }
    }
    return result
}
```



In this Go function, we iterate over the input slice of strings (`strings`) and check if each string starts with the given prefix using the `strings.HasPrefix` function. If it does, we append it to the result slice. Finally, we return the filtered slice.

The time complexity of this function is O(n), where n is the length of the input slice, because we iterate over the slice once. The space complexity is also O(n), because in the worst case, we might need to store all strings in the result slice.