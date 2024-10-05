```go
func CountUpper(s string) int {
    count := 0
    for i, c := range s {
        if i%2 == 0 && strings.ContainsRune("AEIOU", c) {
            count++
        }
    }
    return count
}
```