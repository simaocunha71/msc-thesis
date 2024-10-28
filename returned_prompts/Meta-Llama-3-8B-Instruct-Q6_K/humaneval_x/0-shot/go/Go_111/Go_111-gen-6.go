Here is a simple function that uses a map to count the occurrences of each letter in the string, and then returns a map with the letter(s) that have the maximum count.

```go
import (
    "strings"
    "fmt"
)

func Histogram(test string) map[rune]int {
    // Split the string into individual letters
    words := strings.Split(test, " ")
    counts := make(map[rune]int)

    // Count the occurrences of each letter
    for _, word := range words {
        for _, char := range word {
            counts[char]++
        }
    }

    // Find the maximum count
    maxCount := 0
    maxLetters := make(map[rune]bool)
    for char, count := range counts {
        if count > maxCount {
            maxCount = count
            maxLetters = map[rune]bool{}
            maxLetters[char] = true
        } else if count == maxCount {
            maxLetters[char] = true
        }
    }

    // Convert the maxLetters map to a map with the count
    result := make(map[rune]int)
    for char := range maxLetters {
        result[char] = maxCount
    }

    return result
}

func main() {
    fmt.Println(Histogram("a b c"))  // Output: map[a:1 b:1 c:1]
    fmt.Println(Histogram("a b b a")) // Output: map[a:2 b:2]
    fmt.Println(Histogram("a b c a b")) // Output: map[a:2 b:2]
    fmt.Println(Histogram("b b b b a")) // Output: map[b:4]
    fmt.Println(Histogram("")) // Output: map[]
}
```

In this code, we first split the string into individual words using `strings.Split`. Then we iterate over each word and count the occurrences of each letter using a map. We then find the maximum count and create a new map with the letters that have this maximum count. Finally, we return this new map. In the `main` function, we test the `Histogram` function with different strings and print the results.