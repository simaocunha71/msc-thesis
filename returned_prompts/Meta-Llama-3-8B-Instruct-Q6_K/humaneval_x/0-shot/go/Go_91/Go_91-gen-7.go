```go
package main

import (
    "regexp"
    "strings"
)

func IsBored(S string) int {
    sentences := strings.Split(S, "[.!?]")
    count := 0
    for _, sentence := range sentences {
        sentence = strings.TrimSpace(sentence)
        if len(sentence) > 0 && strings.HasPrefix(sentence, "I") {
            count++
        }
    }
    return count
}

func main() {
    fmt.Println(IsBored("Hello world"))  // 0
    fmt.Println(IsBored("The sky is blue. The sun is shining. I love this weather"))  // 1
}
```
This solution works by splitting the input string into sentences using a regular expression. It then iterates over each sentence, trims any whitespace, and checks if the sentence starts with "I". If it does, it increments a counter. Finally, it returns the count. The main function demonstrates the usage of the IsBored function with the given examples.