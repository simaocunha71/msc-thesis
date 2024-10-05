Here is the solution:

```go
import (
    "math"
    "strings"
    "time"
)

// returns encoded string by cycling groups of three characters.
func EncodeCyclic(s string) string {
    groups := make([]string, 0)
    for i := 0; i < ((len(s) + 2) / 3); i++ {
        groups = append(groups, s[3*i:int(math.Min(float64(3*i+3), float64(len(s))))])
    }
    newGroups := make([]string, 0)
    for _, group := range groups {
        runes := []rune(group)
        if len(group) == 3 {
            newGroups = append(newGroups, string(append(runes[1:], runes[0])))
        } else {
            newGroups = append(newGroups, group)
        }
    }
    return strings.Join(newGroups, "")
}

// takes as input string encoded with EncodeCyclic function. Returns decoded string.
func DecodeCyclic(s string) string {
    result := ""
    for i := 0; i < len(s); i++ {
        if i%3 == 0 && i != 0 {
            result += s[i-1]
        }
        if i%3 == 2 {
            result += s[i]
        }
    }
    return result
}
```

The EncodeCyclic function takes a string as input and returns an encoded string by cycling groups of three characters. It works by splitting the input string into groups of three characters, and then cycling the characters within each group. If a group has less than three characters, it is left unchanged. The encoded string is then returned by concatenating the groups.

The DecodeCyclic function takes an encoded string as input and returns the decoded string. It works by iterating over the encoded string and appending characters to the result string. It checks if the current character is the first or second character of a group of three characters. If it is the first character, it appends the previous character to the result string. If it is the second character, it appends the current character to the result string. If it is the third character, it appends the current character to the result string. The decoded string is then returned.