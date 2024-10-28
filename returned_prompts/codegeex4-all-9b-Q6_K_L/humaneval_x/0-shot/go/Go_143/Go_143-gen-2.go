```go
func WordsInSentence(sentence string) string {
    isPrime := func(n int) bool {
        if n <= 1 {
            return false
        }
        for i := 2; i*i <= n; i++ {
            if n%i == 0 {
                return false
            }
        }
        return true
    }

    words := strings.Fields(sentence)
    var result []string
    for _, word := range words {
        if isPrime(len(word)) {
            result = append(result, word)
        }
    }
    return strings.Join(result, " ")
}
```
