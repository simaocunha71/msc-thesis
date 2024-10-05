Here is a simple Go function that uses the `strings.Split` function to split the input string into words:

```go
package main

import (
    "strings"
)

func WordsString(s string) []string {
    return strings.Split(s, ",| ")
}

func main() {
    fmt.Println(WordsString("Hi, my name is John")) // ["Hi", "my", "name", "is", "John"]
    fmt.Println(WordsString("One, two, three, four, five, six")) // ["One", "two", "three", "four", "five", "six"]
}
```

In this function, `strings.Split` is used to split the input string `s` into words. The second argument to `strings.Split` is a delimiter string, which is used to split the input string. In this case, we use a delimiter string of ",| " to split the input string by both commas and spaces. The result is an array of words, which is returned by the function. 

This function assumes that the input string is a comma-separated list of words, where each word may contain spaces. It also assumes that the input string does not contain any escape sequences or special characters that would affect the splitting process. If you need to handle more complex input strings, you may need to use a more sophisticated splitting algorithm. 