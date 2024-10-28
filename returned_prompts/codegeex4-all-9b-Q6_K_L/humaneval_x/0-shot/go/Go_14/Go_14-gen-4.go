You can use the following code to solve this problem:

```
func AllPrefixes(str string) []string {
    result := []string{}
    for i := 1; i <= len(str); i++ {
        result = append(result, str[:i])
    }
    return result
}
```

This code iterates through the input string and appends all prefixes to the result slice. It starts from index 1 because the first prefix is the first character of the string. The code then appends the substring from index 0 to i to the result slice. Finally, it returns the result slice.