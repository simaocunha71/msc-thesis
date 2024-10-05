Here is a Go solution for the problem:

```go
package main

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

The solution works by first splitting the input sentence into words. Then for each word, it checks if the length of the word is a prime number using the `isPrime` function. If the length is prime, the word is added to the result string. Finally, the result string is trimmed to remove any extra spaces. The `isPrime` function checks if a number is prime by iterating from 2 to the square root of the number and checking if the number is divisible by any of these values. If it is not divisible, the number is prime. The `WordsInSentence` function then returns the resulting string. In the `main` function, we test the `WordsInSentence` function with two different input sentences and print the results. 