Here is the solution to the problem:

```go
func WordsInSentence(sentence string) string {
    words := strings.Split(sentence, " ")
    var result strings.Builder
    for _, word := range words {
        if isPrime(len(word)) {
            result.WriteString(word + " ")
        }
    }
    return strings.TrimSpace(result.String())
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

In this solution, we first split the input sentence into words using the `strings.Split` function. Then, we iterate over each word and check if its length is a prime number using the `isPrime` function. If the length is prime, we add the word to the result string. Finally, we trim the result string to remove the trailing space and return it.

The `isPrime` function checks if a given number is prime by iterating from 2 to the square root of the number and checking if the number is divisible by any of these values. If it is, the function returns `false`. If the number is not divisible by any of these values, the function returns `true`. This function is used in the `WordsInSentence` function to filter out words with non-prime lengths.