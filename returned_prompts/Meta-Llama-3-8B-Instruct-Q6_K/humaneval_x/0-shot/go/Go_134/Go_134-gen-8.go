Here is the solution to the problem:

```go
import (
    "strings"
)

func CheckIfLastCharIsALetter(txt string) bool {
    // Remove trailing spaces
    txt = strings.TrimSpace(txt)
    
    // If the string is empty, return false
    if len(txt) == 0 {
        return false
    }
    
    // Get the last character of the string
    lastChar := txt[len(txt)-1]
    
    // Check if the last character is an alphabetical character
    if !((lastChar >= 'a' && lastChar <= 'z') || (lastChar >= 'A' && lastChar <= 'Z')) {
        return false
    }
    
    // Check if the last character is part of a word
    if i := strings.LastIndex(txt, " "); i >= 0 {
        if i == len(txt)-1 || i == len(txt)-2 {
            return false
        }
    }
    
    // If all conditions are met, return true
    return true
}
```


In this solution, we first remove any trailing spaces from the input string using the `strings.TrimSpace` function. Then, we check if the string is empty. If it is, we return false.

Next, we get the last character of the string using slicing (`txt[len(txt)-1]`).

We then check if the last character is an alphabetical character by checking if it falls within the range of 'a' to 'z' (inclusive) or 'A' to 'Z' (inclusive). If it is not, we return false.

Finally, we check if the last character is part of a word by searching for the last space character in the string using the `strings.LastIndex` function. If the last space character is the last or second-to-last character in the string, we return false.

If all conditions are met, we return true. Otherwise, we return false.