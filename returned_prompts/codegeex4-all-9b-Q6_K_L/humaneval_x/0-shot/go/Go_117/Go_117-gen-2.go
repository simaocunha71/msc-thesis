```go
func SelectWords(s string, n int) []string {
    if len(s) == 0 {
        return []string{}
    }
    words := strings.Fields(s)
    var result []string
    for _, word := range words {
        if countConsonants(word) == n {
            result = append(result, word)
        }
    }
    return result
}

func countConsonants(s string) int {
    count := 0
    for _, c := range s {
        if isConsonant(c) {
            count++
        }
    }
    return count
}

func isConsonant(c rune) bool {
    return !isVowel(c) && (c >= 'a' && c <= 'z' || c >= 'A' && c <= 'Z')
}

func isVowel(c rune) bool {
    return strings.ContainsRune("aeiouAEIOU", c)
}
```
