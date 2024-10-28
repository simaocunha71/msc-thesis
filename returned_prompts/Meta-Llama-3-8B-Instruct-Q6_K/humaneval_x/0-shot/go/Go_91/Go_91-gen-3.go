```go
package main

import (
    "regexp"
    "strings"
)

func IsBored(S string) int {
    // Split the string into sentences
    sentences := regexp.MustCompile(`[.!?]`).Split(strings.TrimSpace(S), -1)

    // Initialize the boredom counter
    boredomCount := 0

    // Iterate over each sentence
    for _, sentence := range sentences {
        // Check if the sentence starts with "I"
        if strings.HasPrefix(strings.TrimSpace(sentence), "I") {
            // If it does, increment the boredom counter
            boredomCount++
        }
    }

    // Return the boredom count
    return boredomCount
}

func main() {
    fmt.Println(IsBored("Hello world"))  // 0
    fmt.Println(IsBored("The sky is blue. The sun is shining. I love this weather"))  // 1
}
```


The code defines a function `IsBored` that takes a string `S` as input and returns the number of boredoms. A boredom is a sentence that starts with the word "I". The function uses a regular expression to split the input string into sentences, and then iterates over each sentence to check if it starts with "I". If it does, it increments a boredom counter. Finally, the function returns the boredom count.

The `main` function demonstrates the usage of the `IsBored` function with two example inputs. The first input is "Hello world", which does not contain any boredoms, so the output is 0. The second input is "The sky is blue. The sun is shining. I love this weather", which contains one boredom (the sentence "I love this weather"), so the output is 1.