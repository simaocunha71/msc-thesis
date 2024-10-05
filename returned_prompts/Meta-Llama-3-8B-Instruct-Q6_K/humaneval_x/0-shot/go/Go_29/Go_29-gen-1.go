```
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


Explanation:
This function takes an input list of strings (`strings`) and a prefix string (`prefix`). It returns a new list that contains only the strings from the input list that start with the given prefix.

Inside the function, we initialize an empty list `result` that will store the filtered strings. We then iterate over the input list using a range loop. For each string `s` in the input list, we check if it starts with the given prefix using the `strings.HasPrefix` function. If it does, we append it to the `result` list using the `append` function. Finally, we return the `result` list.

The time complexity of this function is O(n), where n is the length of the input list, because we iterate over the list once. The space complexity is O(n) as well, because in the worst case, we might need to store all strings in the `result` list.