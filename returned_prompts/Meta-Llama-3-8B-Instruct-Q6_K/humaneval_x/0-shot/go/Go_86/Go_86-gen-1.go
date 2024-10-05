Here is a simple function in Go that accomplishes the task:

```go
import (
    "sort"
    "strings"
)

func AntiShuffle(s string) string {
    words := strings.Split(s, " ")
    for i := 0; i < len(words); i++ {
        word := []byte(words[i])
        sort.Slice(word, func(i, j int) bool {
            return word[i] < word[j]
        })
        words[i] = string(word)
    }
    return strings.Join(words, " ")
}
```

This function works by first splitting the input string into individual words. It then iterates over each word, sorting the characters in ascending order using the `sort.Slice` function. The sorted word is then converted back to a string and replaces the original word in the slice. Finally, the function joins the sorted words back together with spaces in between to form the output string. 

For example, if you call `AntiShuffle("Hello World!!!")`, it will return `"Heellllo !!!Wdlor"`. 

This function assumes that the input string only contains words separated by spaces and does not contain any punctuation marks or special characters. If the input string can contain such characters, you may need to add additional logic to handle them correctly. 