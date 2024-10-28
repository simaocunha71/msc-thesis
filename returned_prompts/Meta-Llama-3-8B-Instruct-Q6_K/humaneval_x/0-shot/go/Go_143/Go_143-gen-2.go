Here is a possible solution in Go:
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
The `isPrime` function checks if a given integer is prime. The `WordsInSentence` function splits the input sentence into words, and then iterates over the words to check if their lengths are prime. If a word's length is prime, it is added to the result string. Finally, the `strings.TrimSpace` function is used to remove any trailing spaces from the result string.

In the `main` function, we test the `WordsInSentence` function with the given examples and print the output. The output should match the expected results.