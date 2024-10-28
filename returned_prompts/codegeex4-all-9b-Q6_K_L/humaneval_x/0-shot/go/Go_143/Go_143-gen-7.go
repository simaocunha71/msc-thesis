```go
func WordsInSentence(sentence string) string {
    // Split the sentence into words
    words := strings.Split(sentence, " ")

    // Initialize an empty string to store the result
    result := ""

    // Check the length of each word
    for _, word := range words {
        // If the length of the word is a prime number, add it to the result
        if isPrime(len(word)) {
            result += word + " "
        }
    }

    // Return the result, removing any trailing spaces
    return strings.TrimSpace(result)
}

// Function to check if a number is prime
func isPrime(n int) bool {
    // 1 is not a prime number
    if n <= 1 {
        return false
    }

    // Check if n is divisible by any number up to its square root
    for i := 2; i*i <= n; i++ {
        if n%i == 0 {
            return false
        }
    }

    // If n is not divisible by any number up to its square root, it is a prime number
    return true
}
```