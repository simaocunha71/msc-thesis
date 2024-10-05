```go
import (
    "strings"
    "regexp"
)

func IsBored(S string) int {
    re := regexp.MustCompile(`I\s.*[.?!]`)
    return len(re.FindAllString(S, -1))
}
```

The regular expression `I\s.*[.?!]` is used to match the sentences that start with the word "I". The `.*` matches any characters (including none) and `[\s.?!]` matches any whitespace, period, question mark or exclamation mark. The `FindAllString` function returns a slice of all the substrings that match the regular expression. The length of this slice is then returned as the number of boredoms.