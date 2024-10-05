```go
func WordsInSentence(sentence string) string {
    primeWords := []string{}
    for _, word := range strings.Fields(sentence) {
        if isPrime(len(word)) {
            primeWords = append(primeWords, word)
        }
    }
    return strings.Join(primeWords, " ")
}

func isPrime(n int) bool {
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
```