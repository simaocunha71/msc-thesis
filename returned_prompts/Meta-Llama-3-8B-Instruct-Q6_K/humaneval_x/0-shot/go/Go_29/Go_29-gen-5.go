```go
func FilterByPrefix(strings []string, prefix string) []string {
    result := make([]string, 0, len(strings))
    for _, s := range strings {
        if strings.HasPrefix(s, prefix) {
            result = append(result, s)
        }
    }
    return result
}
```


The `FilterByPrefix` function takes two inputs: `strings` which is a slice of strings and `prefix` which is the prefix to filter by. It returns a new slice of strings that only includes the strings from the original slice that start with the given prefix.

The function initializes an empty slice `result` with a capacity equal to the length of the `strings` slice. It then iterates over each string `s` in the `strings` slice. If `s` starts with the `prefix` (using the `strings.HasPrefix` function), it appends `s` to the `result` slice. Finally, it returns the `result` slice.

For example, if you call `FilterByPrefix([]string{"abc", "bcd", "cde", "array"}, "a")`, the function will return `["abc", "array"]` because these are the only strings in the input slice that start with the prefix "a". If you call `FilterByPrefix([]string{}, "a")`, the function will return an empty slice because there are no strings in the input slice that start with the prefix "a".