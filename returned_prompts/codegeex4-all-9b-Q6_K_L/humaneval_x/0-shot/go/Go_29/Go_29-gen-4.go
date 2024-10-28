You can use the following code to filter an input list of strings only for ones that start with a given prefix:

```
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

This function takes in two parameters: a slice of strings and a prefix string. It initializes an empty slice called `result` to store the filtered strings.

Then, it loops through each string in the input slice using a `for` loop. For each string, it checks if it starts with the given prefix using the `strings.HasPrefix()` function. If it does, it appends the string to the `result` slice using the `append()` function.

Finally, it returns the `result` slice containing only the strings that start with the given prefix.