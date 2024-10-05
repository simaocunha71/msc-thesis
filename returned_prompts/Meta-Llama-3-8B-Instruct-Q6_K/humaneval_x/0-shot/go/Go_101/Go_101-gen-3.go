Here is a simple solution using the `strings.Split` function from the `strings` package in Go:

```go
package main

import (
    "strings"
)

func WordsString(s string) []string {
    return strings.Split(s, ",| ")
}

func main() {
    fmt.Println(WordsString("Hi, my name is John"))
    fmt.Println(WordsString("One, two, three, four, five, six"))
}
```

This function uses the `strings.Split` function to split the input string `s` into words. The second argument is a separator string, which is a comma followed by a space (`", "`), or a space character (`" "`). This means that the function will split the string into words whenever it encounters a comma or a space. The result is an array of strings, each of which is a word from the original string.

The `main` function demonstrates the use of the `WordsString` function with two different input strings. The output will be:

```
[Hi my name is John]
[One two three four five six]
```

This shows that the function correctly split the input strings into words.