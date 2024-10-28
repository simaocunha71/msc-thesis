```go
func TotalMatch(lst1 []string,lst2 []string) []string {
    sum1, sum2 := 0, 0
    for _, v := range lst1 {
        sum1 += len(v)
    }
    for _, v := range lst2 {
        sum2 += len(v)
    }
    if sum1 <= sum2 {
        return lst1
    } else {
        return lst2
    }
}
```