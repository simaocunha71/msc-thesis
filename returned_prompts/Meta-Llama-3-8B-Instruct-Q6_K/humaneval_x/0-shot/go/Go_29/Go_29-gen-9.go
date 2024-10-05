```go
func FilterByPrefix(strings []string, prefix string) []string {
    result := make([]string, 0)
    for _, str := range strings {
        if strings.HasPrefix(str, prefix) {
            result = append(result, str)
        }
    }
    return result
}
```


This function iterates through the input list of strings and checks if each string starts with the given prefix using the `strings.HasPrefix` function. If it does, the string is added to the result list. The function then returns the result list. The time complexity of this function is O(n), where n is the length of the input list, because it needs to iterate through all elements in the list. The space complexity is also O(n), because in the worst case, all strings might start with the prefix, so the result list would be the same size as the input list.