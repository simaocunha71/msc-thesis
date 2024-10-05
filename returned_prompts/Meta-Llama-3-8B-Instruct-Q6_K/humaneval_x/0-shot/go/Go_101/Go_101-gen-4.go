Here is the solution:

```go
import (
    "strings"
)

func WordsString(s string) []string {
    return strings.Split(s, ", ")
}
```


Explanation:

The `strings.Split` function is used to split the input string `s` into an array of substrings, using the given separator (`", "`) as the delimiter. In this case, the separator is a comma followed by a space, so the function will split the string at each occurrence of this separator. The resulting array of substrings (words) is then returned.