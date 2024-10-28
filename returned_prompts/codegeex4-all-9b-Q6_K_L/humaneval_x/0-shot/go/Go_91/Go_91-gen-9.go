```go
import (
    "regexp"
    "strings"
)

func IsBored(S string) int {
    boredoms := 0
    var re = regexp.MustCompile(`(?i)^I`)
    sentences := strings.Split(S, `\.|\?|!`)
    for _, sentence := range sentences {
        if re.MatchString(strings.TrimSpace(sentence)) {
            boredoms++
        }
    }
    return boredoms
}
```

In the provided Go solution, we are using regular expressions to check if a sentence starts with the word "I" (ignoring case). The `regexp.MustCompile` function compiles a regular expression pattern into a `Regexp` object, which can then be used to match against text.

The `strings.Split` function splits the input string `S` into an array of sentences based on the delimiters `.`, `?`, or `!`. The `strings.TrimSpace` function is used to remove any leading or trailing whitespace from each sentence.

We then iterate through each sentence and use the `MatchString` method of the `Regexp` object to check if the sentence starts with the word "I". If it does, we increment the `boredoms` counter.

Finally, we return the total number of boredoms found in the input string.