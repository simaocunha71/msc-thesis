```go
func GetClosestVowel(word string) string {
    vowels := "aeiouAEIOU"
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
