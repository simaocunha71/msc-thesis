```go
func CountUpper(s string) int {
    upperVowels := map[rune]bool{'A': true, 'E': true, 'I': true, 'O': true, 'U': true}
    count := 0
    for i, c := range s {
        if i%2 == 0 && upperVowels[strings.ToUpper(string(c))] {
            count++
        }
    }
    return count
}
```
