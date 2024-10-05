```go
func OddCount(lst []string) []string {
    result := []string{}
    for i, s := range lst {
        count := 0
        for _, c := range s {
            if (c-'0')%2 != 0 {
                count++
            }
        }
        result = append(result, fmt.Sprintf("the number of odd elements %dn the str%dng %d of the %dnput.", count, count, i+1, count))
    }
    return result
}
```