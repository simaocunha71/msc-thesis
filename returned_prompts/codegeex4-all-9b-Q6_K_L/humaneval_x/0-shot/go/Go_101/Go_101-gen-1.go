You can use the `strings.Fields` function to split the string into words. Here's a possible implementation:

```go
import (
    "strings"
)

func WordsString(s string) []string {
    return strings.Fields(s)
}
```

The `strings.Fields` function splits the string into words using the default space characters (space, tab, and newline) as separators. If you want to use a different separator, you can use the `strings.Split` function instead:

```go
import (
    "strings"
)

func WordsString(s string) []string {
    return strings.Split(s, ", ")
}
```

This will split the string into words using the comma and space characters as separators.