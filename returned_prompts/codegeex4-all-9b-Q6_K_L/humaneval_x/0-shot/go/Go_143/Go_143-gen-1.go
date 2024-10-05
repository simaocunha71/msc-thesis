```go
func WordsInSentence(sentence string) string {
    words := strings.Fields(sentence)
    var result []string
    for _, word := range words {
        if isPrime(len(word)) {
            result = append(result, word)
        }
    }
    return strings.Join(result, " ")
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
The `WordsInSentence` function takes a sentence as input, splits it into words, and returns a string that contains only the words whose lengths are prime numbers. The `isPrime` function checks if a number is prime.