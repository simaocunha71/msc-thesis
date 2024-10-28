Here is the solution:
```go
import (
    "strings"
)

func WordsString(s string) []string {
    return strings.Split(s, ", | ")
}
```
Explanation:
The `strings.Split` function takes a string and a separator as input, and returns a slice of strings that are split by the separator. The separator can be a single character or a string.

In this case, we use a separator that is a comma followed by a space (`", | "`). This will split the input string into words, even if they are separated by commas or spaces.

For example, if the input string is "Hi, my name is John", the `strings.Split` function will split it into the words "Hi", "my", "name", "is", and "John". Similarly, if the input string is "One, two, three, four, five, six", the function will split it into the words "One", "two", "three", "four", "five", and "six".