```go
func WordsInSentence(sentence string) string {
    // split the sentence into words
    words := strings.Split(sentence, " ")
    
    // define a helper function to check if a number is prime
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
    
    // filter the words whose lengths are prime numbers
    var result []string
    for _, word := range words {
        if isPrime(len(word)) {
            result = append(result, word)
        }
    }
    
    // join the filtered words into a string
    return strings.Join(result, " ")
}
```