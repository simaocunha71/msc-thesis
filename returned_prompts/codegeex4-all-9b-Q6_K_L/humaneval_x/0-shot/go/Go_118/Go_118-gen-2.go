```go
func GetClosestVowel(word string) string {
    vowels := "AEIOUaeiou"
    for i := len(word) - 2; i > 0; i-- {
        if strings.Contains(vowels, string(word[i])) {
            if !strings.Contains(vowels, string(word[i-1])) && !strings.Contains(vowels, string(word[i+1])) {
                return string(word[i])
            }
        }
    }
    return ""
}
```
