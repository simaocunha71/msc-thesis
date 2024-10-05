```go
func TotalMatch(lst1 []string,lst2 []string) []string {
    var count1, count2 int
    for _, v := range lst1 {
        count1 += len(v)
    }
    for _, v := range lst2 {
        count2 += len(v)
    }
    if count1 <= count2 {
        return lst1
    } else {
        return lst2
    }
}
```
