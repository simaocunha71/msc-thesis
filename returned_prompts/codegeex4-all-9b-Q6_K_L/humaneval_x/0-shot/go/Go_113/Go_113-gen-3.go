```go
func OddCount(lst []string) []string {
    var result []string
    for _, str := range lst {
        count := 0
        for _, ch := range str {
            if (ch-'0')%2 == 1 {
                count++
            }
        }
        result = append(result, fmt.Sprintf("the number of odd elements %dn the str%ng %d of the %dnput.", count, count, count, count))
    }
    return result
}
```

This solution iterates over each string in the input list and counts the number of odd digits in each string. It then formats a new string using the count and appends it to the result list. Finally, it returns the result list.