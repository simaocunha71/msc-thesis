Here is the solution in Go:

```go
import (
    "strings"
    "fmt"
)

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

func WordsInSentence(sentence string) string {
    words := strings.Split(sentence, " ")
    result := ""
    for _, word := range words {
        if isPrime(len(word)) {
            result += word + " "
        }
    }
    return strings.TrimSpace(result)
}

func main() {
    fmt.Println(WordsInSentence("This is a test")) // Output: "is"
    fmt.Println(WordsInSentence("lets go for swimming")) // Output: "go for"
}
```

In this solution, we first split the input sentence into words using the `strings.Split` function. Then, for each word, we check if its length is a prime number using the `isPrime` function. If it is, we add the word to the result string. Finally, we return the result string after trimming any trailing spaces using the `strings.TrimSpace` function.

The `isPrime` function checks if a given number is prime by iterating from 2 to the square root of the number and checking if the number is divisible by any of these values. If it is, the function returns `false`, indicating that the number is not prime. If the number is not divisible by any of these values, the function returns `true`, indicating that the number is prime.

The `WordsInSentence` function is the main function that takes a sentence as input and returns a string containing the words from the original sentence whose lengths are prime numbers. It uses the `isPrime` function to check if a word's length is prime and adds the word to the result string if it is. Finally, it returns the result string after trimming any trailing spaces.