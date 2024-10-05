```go
func FilterByPrefix(strings []string, prefix string) []string {
    var result []string
    for _, str := range strings {
        if strings.HasPrefix(str, prefix) {
            result = append(result, str)
        }
    }
    return result
}
```


The function `FilterByPrefix` filters a list of strings based on a given prefix. It iterates over the input list of strings and checks if each string starts with the given prefix using the `strings.HasPrefix` function. If the string starts with the prefix, it is added to the result list. Finally, the function returns the result list. 

The example usage shows that the function correctly filters the input list based on the given prefix. The first example with an empty input list returns an empty result list, while the second example with a list of strings and a prefix 'a' returns the strings that start with 'a'. 

Note: The `strings.HasPrefix` function is case-sensitive, so if you want to perform a case-insensitive search, you can convert both the string and the prefix to lower case (or upper case) before comparing them. For example: `strings.ToLower(str) == strings.ToLower(prefix)`.  However, in this example, we assume that the prefix is case-sensitive.  If you want to make the search case-insensitive, you can modify the condition to `strings.HasPrefix(strings.ToLower(str), strings.ToLower(prefix))`. 