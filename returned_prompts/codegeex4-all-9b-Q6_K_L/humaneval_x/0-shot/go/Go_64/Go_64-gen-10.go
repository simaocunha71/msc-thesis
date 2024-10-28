```go
func VowelsCount(s string) int {
    vowels := map[rune]bool{'a': true, 'e': true, 'i': true, 'o': true, 'u': true, 'A': true, 'E': true, 'I': true, 'O': true, 'U': true, 'Y': true}
    count := 0
    for _, c := range s {
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
