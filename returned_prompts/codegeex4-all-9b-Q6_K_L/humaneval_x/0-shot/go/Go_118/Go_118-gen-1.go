```go
func GetClosestVowel(word string) string {
    vowels := "AEIOUaeiou"
    for i := len(word) - 2; i > 0; i-- {
        if vowels.Contains(string(word[i])) &&
            !vowels.Contains(string(word[i-1])) &&
            !vowels.Contains(string(word[i+1])) {
            return string(word[i])
        }
    }
    return ""
}

func (s string) Contains(substring string) bool {
    return bytes.Contains([]byte(s), []byte(substring))
}
```
