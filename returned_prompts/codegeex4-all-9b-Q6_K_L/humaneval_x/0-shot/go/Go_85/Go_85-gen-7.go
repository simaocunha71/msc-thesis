```go
func Add(lst []int) int {
    sum := 0
    for i := 0; i < len(lst); i += 2 {
        if lst[i] % 2 == 0 {
            sum += lst[i]
        }
    }
    return sum
}
```
