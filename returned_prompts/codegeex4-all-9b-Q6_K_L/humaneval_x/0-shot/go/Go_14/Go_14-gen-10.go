You can achieve this with a simple loop and append the current character to the previous prefix. Here's how you can do it:

```go
func AllPrefixes(str string) []string {
    prefixes := make([]string, 0, len(str))
    for i := 1; i <= len(str); i++ {
        prefixes = append(prefixes, str[:i])
    }
    return prefixes
}
```

In this function, we initialize an empty slice `prefixes` with a length equal to the length of the input string `str`. Then, we iterate from 1 to the length of `str` and for each iteration, we append the prefix of `str` up to the current index `i` to the `prefixes` slice. Finally, we return the `prefixes` slice.

This will give you the list of all prefixes from shortest to longest of the input string. For example, calling `AllPrefixes("abc")` will return `["a", "ab", "abc"]`.