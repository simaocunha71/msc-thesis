```go
func OddCount(lst []string) []string {
    var result []string
    for i, s := range lst {
        count := 0
        for _, c := range s {
            if (c-'0')%2 != 0 {
                count++
            }
        }
        result = append(result, fmt.Sprintf("the number of odd elements %dn the str%ng %d of the %dnput.", count, count, i, count))
    }
    return result
}
```