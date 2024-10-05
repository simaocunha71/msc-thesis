Here is a Go function that solves the problem:
```go
func GetClosestVowel(word string) string {
    for i := len(word) - 1; i >= 0; i-- {
        c := word[i]
        if c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' ||
            c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U' {
            if i > 0 && !isConsonant(word[i-1]) {
                return string(c)
            }
