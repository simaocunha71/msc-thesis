Here is the solution:
```go
import (
    "strings"
)

func WordsString(s string) []string {
    return strings.Split(s, " ")
}
```
Explanation:

The `strings.Split` function is used to split the input string `s` into words separated by the specified separator, which in this case is a space character `" "`. The resulting array of words is returned.

Note that the `strings.Split` function splits the input string into substrings separated by the specified separator, and returns an array of these substrings. The separator is not included in the resulting substrings.

For example, if the input string is `"Hi, my name is John"`, the `strings.Split` function will split it into the following substrings: `["Hi,", "my", "name", "is", "John"]`. The comma character is not included in the resulting substrings.

If you want to split the input string by both commas and spaces, you can use the `strings.Split` function with a separator that is a combination of both, like this:
```go
func WordsString(s string) []string {
    return strings.Split(strings.ReplaceAll(s, ",", " "), " ")
}
```
This will first replace all comma characters with space characters, and then split the resulting string into words separated by space characters. The resulting array of words will be `["Hi", "my", "name", "is", "John"]`.