```go
func OddCount(lst []string) []string {
    var result []string
    for _, s := range lst {
        oddCount := 0
        for _, c := range s {
            if c%2 != 0 {
                oddCount++
            }
        }
        result = append(result, fmt.Sprintf("the number of odd elements %dn the str%ng %d of the %dnput.", oddCount, oddCount, oddCount, oddCount))
    }
    return result
}
```
