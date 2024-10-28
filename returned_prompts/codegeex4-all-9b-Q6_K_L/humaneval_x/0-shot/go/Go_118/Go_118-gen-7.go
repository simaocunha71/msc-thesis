```go
func GetClosestVowel(word string) string {
    vowels := map[rune]bool{'a': true, 'e': true, 'i': true, 'o': true, 'u': true, 'A': true, 'E': true, 'I': true, 'O': true, 'U': true}
    n := len(word)
    for i := n - 1; i >= 1; i-- {
        if !vowels[rune(word[i])] && vowels[rune(word[i-1])] {
            return string(rune(word[i-1]))
        }
    }
    return ""
}
```
