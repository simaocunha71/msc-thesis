```go
func GetClosestVowel(word string) string {
    vowels := map[rune]bool{
        'a': true,
        'e': true,
        'i': true,
        'o': true,
        'u': true,
        'A': true,
        'E': true,
        'I': true,
        'O': true,
        'U': true,
    }
    for i := len(word) - 2; i > 0; i-- {
        if !vowels[rune(word[i])] && vowels[rune(word[i-1])] && vowels[rune(word[i+1])] {
            return string(word[i])
        }
    }
    return ""
}
```
