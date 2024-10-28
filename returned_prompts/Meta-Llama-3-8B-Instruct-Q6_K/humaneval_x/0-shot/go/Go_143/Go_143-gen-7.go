Here is the solution to the problem:

```go
import (
    "strings"
    "math"
)

func WordsInSentence(sentence string) string {
    words := strings.Split(sentence, " ")
    var result strings.Builder
    for _, word := range words {
        length := len(word)
        if isPrime(length) {
            result.WriteString(word + " ")
        }
    }
    return strings.TrimSpace(result.String())
}

func isPrime(n int) bool {
    if n <= 1 {
        return false
    }
    for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
        if n%i == 0 {
            return false
        }
    }
    return true
}
```
In this solution, we first split the input sentence into words using the `strings.Split` function. Then, we iterate over each word and check if its length is a prime number using the `isPrime` function. If the length is prime, we add the word to the result string builder. Finally, we return the result string after trimming any trailing spaces.

The `isPrime` function checks if a given number is prime by iterating from 2 to the square root of the number and checking if the number is divisible by any of these values. If it is, then the number is not prime and the function returns `false`. If the number is not divisible by any of these values, then it is prime and the function returns `true`. This function is used to filter out words with lengths that are not prime numbers.