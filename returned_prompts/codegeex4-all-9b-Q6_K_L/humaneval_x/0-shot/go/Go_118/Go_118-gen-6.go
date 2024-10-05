```go
func GetClosestVowel(word string) string {
    vowels := map[byte]bool{'a': true, 'e': true, 'i': true, 'o': true, 'u': true, 'A': true, 'E': true, 'I': true, 'O': true, 'U': true}
    for i := len(word) - 2; i >= 0; i-- {
        if _, ok := vowels[word[i]]; ok && !vowels[word[i+1]] && !vowels[word[i+2]] {
            return string(word[i])
        }
    }
    return ""
}
```
