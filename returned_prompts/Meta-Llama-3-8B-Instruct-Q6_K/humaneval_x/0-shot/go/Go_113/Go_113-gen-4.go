Here is the Go function that meets the requirements:

```go
func OddCount(lst []string) []string {
    var result []string
    for _, s := range lst {
        count := 0
        for _, c := range s {
            if c % 2 != 0 {
                count++
            }
        }
        result = append(result, fmt.Sprintf("the number of odd elements %dn the str%dng %d of the %dnput.", count, len(s), len(s), len(s)))
    }
    return result
}
```

The function iterates over each string in the input list. For each string, it counts the number of odd digits using a nested loop. Then it appends a formatted string to the result list, where the number of odd digits is replaced by the count. The formatted string includes the number of odd digits, the length of the string, and the length of the input list, as required. Finally, the function returns the result list. 