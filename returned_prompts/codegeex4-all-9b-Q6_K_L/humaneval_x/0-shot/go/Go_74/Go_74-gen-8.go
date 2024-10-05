```go
func TotalMatch(lst1 []string,lst2 []string) []string {
    count1 := 0
    for _, str := range lst1 {
        count1 += len(str)
    }
    count2 := 0
    for _, str := range lst2 {
        count2 += len(str)
    }
    if count1 <= count2 {
        return lst1
    } else {
        return lst2
    }
}
```