```go
func GetClosestVowel(word string) string {
    vowels := []byte{'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    for i := len(word) - 1; i >= 1; i-- {
        if bytes.Contains(vowels, word[i]) {
            if !bytes.Contains(vowels, word[i-1]) && !bytes.Contains(vowels, word[i+1]) {
                return string(word[i])
            }
        }
    }
    return ""
}
```
