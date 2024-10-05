Here's a solution to your problem:

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

This solution works by splitting the input sentence into a slice of words using `strings.Fields(sentence)`. Then it iterates over each word, checking if the length of the word is a prime number using the `isPrime` function. If the length of a word is a prime number, it's added to the `result` slice. Finally, the words in the `result` slice are joined back together into a single string using `strings.Join(result, " ")` and returned.