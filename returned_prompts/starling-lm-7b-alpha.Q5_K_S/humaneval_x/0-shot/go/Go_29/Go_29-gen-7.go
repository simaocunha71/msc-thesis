
To filter an input list of strings only for ones that start with a given prefix, you can use the following function in Go:

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

This function takes in two parameters: `strings` (the input list of strings) and `prefix` (the desired prefix). It initializes an empty slice called `result` to store the filtered strings. Then, it iterates over each string in the input list using a `for` loop and checks if the string starts with the given prefix using the `strings.HasPrefix()` function. If the condition is true, the string is appended to the `result` slice. Finally, the function returns the `result` slice containing only the strings that start with the given prefix.

You can test the function with the provided examples:

```go
FilterByPrefix([]string{}, "a") // []
FilterByPrefix([]string{"abc", "bcd", "cde", "array"}, "a") // ["abc", "array"]
```

The first example returns an empty slice because there are no strings in the input list that start with the prefix "a". The second example returns `["abc", "array"]` because these are the only two strings in the input list that start with the prefix "a".

I hope this helps! Let me know if you have any more questions.

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

This function takes in two parameters: `strings` (the input list of strings) and `prefix` (the desired prefix). It initializes an empty slice called `result` to store the filtered strings. Then, it iterates over each string in the input list using a `for` loop and checks if the string starts with the given prefix using the `strings.HasPrefix