
The last question is asking for a function that splits a string based on the following rules:

If the string contains a space, split the string on spaces.
If the string contains a comma, split the string on commas.
Otherwise, return the number of lowercase letters in the string that are in odd positions in the alphabet.

Here's how you could implement this function in Go:

```go
import (
    "strings"
    "unicode"
)

func SplitWords(txt string) interface{} {
    // Split on spaces if they exist
    if strings.Contains(txt, " ") {
        return strings.Split(txt, " ")
    // Split on commas if they exist
    } else if strings.Contains(txt, ",") {
        return strings.Split(txt, ",")
    // Otherwise, count the number of lowercase letters in odd positions
    } else {
        count := 0
        for _, r := range txt {
            if unicode.IsLower(r) && int(r-'a')%2 == 1 {
                count++
            }
        }
        return count
    }
}
```

This function first checks if the string contains spaces or commas. If it does, it splits the string on those characters and returns the resulting slice of strings. If the string does not contain spaces or commas, it counts the number of lowercase letters in odd positions in the alphabet and returns that count.