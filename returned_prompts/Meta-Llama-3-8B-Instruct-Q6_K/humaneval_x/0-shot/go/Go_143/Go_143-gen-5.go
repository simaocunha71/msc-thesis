Here is the solution for the problem:

```go
import (
    "strings"
    "fmt"
)

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

func isPrime(n int) bool {
    if n <= 1 {
        return false
    }
    for i := 2; i * i <= n; i++ {
        if n%i == 0 {
            return false
        }
    }
    return true
}

func main() {
    fmt.Println(WordsInSentence("This is a test"))  // Output: "is"
    fmt.Println(WordsInSentence("lets go for swimming"))  // Output: "go for"
}
```

In this solution, we first split the sentence into words using the `strings.Split` function. Then we iterate over each word and check if its length is a prime number using the `isPrime` function. If it is, we add the word to the result string. Finally, we trim the result string to remove any trailing spaces using the `strings.TrimSpace` function. The `isPrime` function checks if a number is prime by iterating from 2 to the square root of the number and checking if it is divisible by any of these numbers. If it is not divisible, it is a prime number. The `main` function tests the `WordsInSentence` function with two example sentences.