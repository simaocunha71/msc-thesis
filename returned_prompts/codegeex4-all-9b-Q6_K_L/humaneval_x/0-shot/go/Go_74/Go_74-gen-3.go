```go
func TotalMatch(lst1 []string,lst2 []string) []string {
    if len(lst1) == 0 && len(lst2) == 0 {
        return lst1
    }
    if len(lst1) == 0 {
        return lst2
    }
    if len(lst2) == 0 {
        return lst1
    }
    var count1, count2 int
    for _, s := range lst1 {
        count1 += len(s)
    }
    for _, s := range lst2 {
        count2 += len(s)
    }
    if count1 < count2 {
        return lst1
    }
    return lst2
}
```