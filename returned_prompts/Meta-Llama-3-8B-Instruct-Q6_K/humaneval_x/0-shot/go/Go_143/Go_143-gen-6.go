```go
import (
    "strings"
    "math"
)

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
    for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
        if n%i == 0 {
            return false
        }
    }
    return true
}
```


Explanation:
The function `WordsInSentence` takes a sentence as input and returns a new string that contains only the words from the original sentence whose lengths are prime numbers. It splits the sentence into words using the `strings.Split` function, then iterates over each word. For each word, it checks if the length of the word is prime using the `isPrime` function. If the length is prime, it appends the word to a result string builder. Finally, it trims the result string and returns it.

The `isPrime` function checks if a given number is prime by iterating from 2 to the square root of the number and checking if the number is divisible by any of these values. If it is divisible, it returns false; otherwise, it returns true.

The `WordsInSentence` function uses the `isPrime` function to filter out words whose lengths are not prime, and returns the resulting string. The order of the words in the result string is the same as the original sentence, since the `isPrime` function is called for each word in the original order. 