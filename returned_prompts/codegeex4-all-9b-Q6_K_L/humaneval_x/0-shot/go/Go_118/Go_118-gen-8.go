```go
func GetClosestVowel(word string) string {
    vowels := "AEIOUaeiou"
    for i := len(word) - 1; i >= 0; i-- {
        if strings.ContainsRune(vowels, rune(word[i])) {
            if i > 0 && !strings.ContainsRune(vowels, rune(word[i-1])) && i < len(word) - 1 && !strings.ContainsRune(vowels, rune(word[i+1])) {
                return string(word[i])
            }
        }
    }
    return ""
}
```
