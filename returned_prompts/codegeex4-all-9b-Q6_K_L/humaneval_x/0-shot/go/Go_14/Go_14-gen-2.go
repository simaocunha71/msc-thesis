Here is a solution using a simple loop to iterate over the string:

```go
func AllPrefixes(str string) []string {
    prefixes := make([]string, 0, len(str))
    for i := 1; i <= len(str); i++ {
        prefixes = append(prefixes, str[:i])
    }
    return prefixes
}
```

This solution creates an empty slice of strings with a length equal to the input string. It then uses a loop to iterate over the input string and append each prefix to the slice. The `str[:i]` syntax is used to get a substring of the input string from the beginning up to the ith character. This is equivalent to using the `str.Slice(0, i)` method in other programming languages.

The `make` function is used to create the slice with a capacity equal to the length of the input string. This is an optimization to avoid multiple allocations as the slice grows.