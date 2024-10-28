```go
func HowManyTimes(str string,substring string) int{
    count := 0
    for i := 0; i < len(str); i++ {
        if str[i:i+len(substring)] == substring {
            count++
            i += len(substring) - 1
        }
    }
    return count
}
```
