Here is the solution:

```go
import (
    "strings"
)

func CheckIfLastCharIsALetter(txt string) bool {
    // Split the string into words
    words := strings.Fields(txt)
    // Check if the last character is an alphabetical character
    if len(words) > 0 && strings.IndexRune(words[len(words)-1], ' ') == len(words[len(words)-1]) - 1 {
        // If the last word ends with a space, return false
        return false
    } else if len(txt) > 0 && !strings.IsLetter(rune(txt[len(txt)-1])) {
        // If the last character is not an alphabetical character, return false
        return false
    }
    // If the last character is an alphabetical character and is not a part of a word, return true
    return true
}
```



This function first splits the input string into words using the `strings.Fields` function. Then it checks if the last word ends with a space. If it does, the function returns `false` because the last character is not a part of a word.

If the last word does not end with a space, the function checks if the last character of the input string is an alphabetical character using the `strings.IsLetter` function. If it is not, the function returns `false`.

If the last character is an alphabetical character and is not a part of a word, the function returns `true`. If the input string is empty, the function also returns `false` because there is no last character to check.