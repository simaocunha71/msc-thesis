```go
func OddCount(lst []string) []string {
    for i := range lst {
        var count int
        for _, v := range lst[i] {
            if (v-'0')%2 == 1 {
                count++
            }
        }
        lst[i] = fmt.Sprintf("the number of odd elements %dn the str%ng %d of the %dnput.", count, count, count, count)
    }
    return lst
}
```