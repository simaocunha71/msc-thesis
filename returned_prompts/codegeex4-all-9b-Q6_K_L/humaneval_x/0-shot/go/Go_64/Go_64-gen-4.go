```go
func VowelsCount(s string) int {
    vowelMap := map[rune]bool{
        'a': true,
        'e': true,
        'i': true,
        'o': true,
        'u': true,
        'y': true,
    }

    count := 0
    for _, c := range strings.ToLower(s) {
        if vowelMap[c] {
            count++
        }
    }

    return count
}
```
