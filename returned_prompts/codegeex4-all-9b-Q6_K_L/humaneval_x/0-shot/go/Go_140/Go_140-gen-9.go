You can use the strings.Replace function to replace spaces with underscores. Then use a regular expression to replace more than two consecutive underscores with a single dash. Here's how you can do it:

```go
import (
    "strings"
    "regexp"
)

func FixSpaces(text string) string {
    text = strings.Replace(text, " ", "_", -1)
    re := regexp.MustCompile(`_+`)
    text = re.ReplaceAllString(text, "-")
    return text
}
```
The strings.Replace function replaces all spaces in the text with underscores. The regexp.MustCompile function compiles a regular expression, and the re.ReplaceAllString function replaces all occurrences of the regular expression in the text with a single dash.