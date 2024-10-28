Here is the solution in Go:
```go
package main

import (
    "regexp"
    "strings"
)

func IsBored(S string) int {
    sentences := regexp.MustCompile(`[.?!]+`).FindAllString(S, -1)
    boredomCount := 0
    for _, sentence := range sentences {
        if strings.HasPrefix(strings.TrimSpace(sentence), "I") {
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
Explanation:

* We use a regular expression to split the input string into sentences. The regular expression `[.?!]+` matches one or more occurrences of `.`, `?`, or `!`.
* We then iterate over the sentences and check if each sentence starts with the word "I". We use the `strings.HasPrefix` function to do this.
* If a sentence starts with "I", we increment the boredom count.
* Finally, we return the boredom count.

Note that this solution assumes that sentences are separated by `.`, `?`, or `!` and that words are separated by spaces. It also assumes that the input string only contains ASCII characters. If the input string can contain non-ASCII characters or other types of sentence separators, you may need to modify the regular expression and/or the solution accordingly.