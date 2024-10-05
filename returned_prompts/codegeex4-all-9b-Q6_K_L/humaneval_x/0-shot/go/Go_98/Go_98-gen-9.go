```go
func CountUpper(s string) int {
    count := 0
    for i, char := range s {
        if i%2 == 0 && strings.ContainsRune("AEIOU", char) {
            count++
        }
    }
    return count
}
```