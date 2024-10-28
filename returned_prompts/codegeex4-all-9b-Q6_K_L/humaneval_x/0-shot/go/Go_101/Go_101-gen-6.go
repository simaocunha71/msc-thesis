Here's how you can write this function in Go:

```go
import (
    "strings"
)

func WordsString(s string) []string {
    return strings.Split(s, ", ")
}
```

This function uses the `Split` function from the `strings` package to split the input string at each comma followed by a space. It returns an array of the words.