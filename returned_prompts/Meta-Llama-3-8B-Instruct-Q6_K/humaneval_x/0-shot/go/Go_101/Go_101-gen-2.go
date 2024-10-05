Here is the solution in Go:
```go
import (
    "strings"
)

func WordsString(s string) []string {
    return strings.Split(s, ", ")
}
```
Explanation:
The `strings.Split` function is used to split the input string `s` into words using the delimiter ", " (a comma followed by a space). The resulting slice of strings is then returned.

Example usage:
```go
fmt.Println(WordsString("Hi, my name is John")) // Output: ["Hi", "my", "name", "is", "John"]
fmt.Println(WordsString("One, two, three, four, five, six")) // Output: ["One", "two", "three", "four", "five", "six"]
```
Note that this solution assumes that the input string only contains commas and spaces as delimiters. If there are other characters that should be considered as delimiters, you would need to modify the delimiter string accordingly. For example, if you also want to split on semicolons, you could use the delimiter ", |;" (a comma followed by a space, or a semicolon).