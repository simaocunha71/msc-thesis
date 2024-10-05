Here is the solution:

```go
func FilterByPrefix(strings []string, prefix string) []string {
    var result []string
    for _, s := range strings {
        if strings.HasPrefix(s, prefix) {
            result = append(result, s)
        }
    }
    return result
}
```

Explanation:
The `FilterByPrefix` function takes two inputs: `strings` which is a slice of strings, and `prefix` which is a string. The function returns a new slice of strings that contains only the strings from the original slice that start with the given prefix.

The function iterates over each string in the input slice using a for loop. For each string, it checks if the string starts with the given prefix using the `strings.HasPrefix` function. If the string starts with the prefix, it appends the string to the result slice.

Finally, the function returns the result slice, which contains only the strings that start with the given prefix. If no strings start with the prefix, the function returns an empty slice.