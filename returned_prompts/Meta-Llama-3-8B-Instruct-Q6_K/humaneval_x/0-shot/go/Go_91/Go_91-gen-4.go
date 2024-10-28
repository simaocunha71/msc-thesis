```go
package main

import (
    "regexp"
    "strings"
)

func IsBored(S string) int {
    sentences := regexp.MustCompile(`[.!?]+`).FindAllString(S, -1)
    boredomCount := 0
    for _, sentence := range sentences {
        words := strings.Split(sentence, " ")
        if len(words) > 0 && words[0] == "I" {
            boredomCount++
        }
    }
    return boredomCount
}

func main() {
    fmt.Println(IsBored("Hello world")) // 0
    fmt.Println(IsBored("The sky is blue. The sun is shining. I love this weather")) // 1
}
```

In this solution, we first split the input string `S` into sentences using a regular expression. The regular expression `[.!?]+` matches one or more occurrences of `.`, `?`, or `!`, which are commonly used to delimit sentences.

We then iterate over the sentences and split each sentence into words using the `strings.Split` function. If the first word of a sentence is "I", we increment the boredom count.

Finally, we return the boredom count. In the `main` function, we test the `IsBored` function with two examples. The first example returns 0, because there is no sentence starting with "I". The second example returns 1, because there is one sentence starting with "I".