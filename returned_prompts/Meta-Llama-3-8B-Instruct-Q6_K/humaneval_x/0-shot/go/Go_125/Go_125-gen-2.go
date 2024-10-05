Here is the solution:
```go
import (
    "strings"
    "unicode"
)

func SplitWords(txt string) interface{} {
    words := strings.Split(txt, " ")
    if len(words) == 1 && strings.Contains(txt, ",") {
        words = strings.Split(txt, ",")
    }
    if len(words) == 1 {
        count := 0
        for i := 0; i < len(txt); i++ {
            if unicode.IsLower(rune(txt[i])) && (i%2 == 1) {
                count++
            }
        }
        return count
    }
    return words
}
```
Here's an explanation of the code:

1. We first split the input string `txt` on whitespace using `strings.Split`.
2. If the resulting slice has only one element and the original string contains a comma, we split on commas instead.
3. If the resulting slice still has only one element, we count the number of lower-case letters with odd order in the alphabet. We use `unicode.IsLower` to check if a character is lower-case and `rune(txt[i])` to get the ASCII value of the character. We increment the count only if the character is lower-case and has an odd index (i.e., `i%2 == 1`).
4. If the slice has more than one element, we return the slice as is.

Note that we use the `interface{}` type to return the result, which can be either a slice of strings or an integer. This is because the problem statement allows for two different return types depending on the input.