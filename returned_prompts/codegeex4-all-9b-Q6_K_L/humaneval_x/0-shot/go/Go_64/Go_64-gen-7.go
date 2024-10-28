```go
func VowelsCount(s string) int {
    vowels := map[rune]bool{
        'a': true,
        'e': true,
        'i': true,
        'o': true,
        'u': true,
        'y': true,
    }

    count := 0
    for _, c := range strings.ToLower(s) {
        if _, ok := vowels[c]; ok {
            count++
        }
    }

    if len(s) > 0 && s[len(s)-1] == 'y' {
        count++
    }

    return count
}
```