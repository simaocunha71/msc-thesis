Here is a solution in Go:

```go
func Longest(strings []string) interface{}{
    if len(strings) == 0 {
        return nil
    }
    maxLen := len(strings[0])
    maxStr := strings[0]
    for _, str := range strings {
        if len(str) > maxLen {
            maxLen = len(str)
            maxStr = str
        }
    }
    return maxStr
}
```

This function first checks if the input list is empty. If it is, it returns nil. Otherwise, it initializes the longest string (`maxStr`) and the length of the longest string (`maxLen`) to the first string in the list. Then it iterates over the rest of the strings in the list. If it finds a string that is longer than the current longest string, it updates `maxStr` and `maxLen`. Finally, it returns `maxStr`, which is the longest string in the list.

The time complexity of this function is O(n), where n is the number of strings in the list, because it needs to iterate over all of the strings in the list. The space complexity is O(1), because it only uses a constant amount of additional memory.