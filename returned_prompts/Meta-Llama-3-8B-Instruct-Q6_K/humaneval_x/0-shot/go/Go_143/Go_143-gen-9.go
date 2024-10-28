Here is the solution in Golang:
```go
package main

import (
    "strings"
    "math"
)

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
    sentence := "This is a test"
    fmt.Println(WordsInSentence(sentence)) // Output: "is"
    
    sentence = "lets go for swimming"
    fmt.Println(WordsInSentence(sentence)) // Output: "go for"
}
```
This solution splits the input sentence into words and then checks each word's length to see if it's a prime number. If the word's length is a prime number, it's added to the result string. The `isPrime` function checks if a number is prime by iterating from 2 to the square root of the number and checking for divisibility. Finally, the `WordsInSentence` function returns the result string with trailing spaces removed. The `main` function demonstrates the usage of the `WordsInSentence` function with two example sentences.