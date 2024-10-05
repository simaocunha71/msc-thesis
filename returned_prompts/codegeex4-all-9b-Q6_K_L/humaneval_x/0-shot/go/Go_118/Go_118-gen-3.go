```go
func GetClosestVowel(word string) string {
    vowels := "AEIOUaeiou"
    for i := len(word) - 2; i >= 1; i-- {
        if strings.ContainsRune(vowels, rune(word[i])) {
            if !strings.ContainsRune(vowels, rune(word[i-1])) && !strings.ContainsRune(vowels, rune(word[i+1])) {
                return string(word[i])
            }
        }
    }
    return ""
}
```
