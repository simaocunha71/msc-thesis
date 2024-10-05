You can use the following solution in Go:

```go
package main

import (
    "regexp"
    "strings"
)

func IsBored(S string) int {
    sentences := strings.Split(S, "[.!?]")
    var boredoms int
    for _, sentence := range sentences {
        sentence = strings.TrimSpace(sentence)
        if len(sentence) > 0 && strings.HasPrefix(sentence, "I") {
            boredoms++
        }
    }
    return boredoms
}

func main() {
    fmt.Println(IsBored("Hello world")) // 0
    fmt.Println(IsBored("The sky is blue. The sun is shining. I love this weather")) // 1
}
```

This program splits the input string into sentences based on the characters '.', '?', and '!'. Then it iterates over each sentence, trims any leading or trailing spaces, and checks if the sentence starts with "I". If it does, it increments the boredom count. Finally, it returns the total boredom count.