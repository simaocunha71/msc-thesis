To solve this problem we can follow these steps:

1. Check if the string contains any whitespace characters. If it does, we can use the split function to separate the words.
2. If the string does not contain any whitespace characters, we can check if it contains any commas. If it does, we can use the split function to separate the words based on the commas.
3. If the string does not contain any whitespace characters or commas, we can use a regular expression to find all the lowercase letters with odd order in the alphabet and return the count.
4. Here's a sample implementation of the solution in Go:

```go
package main

import (
    "fmt"
    "strings"
    "unicode"
)

func SplitWords(txt string) interface{} {
    if strings.Contains(txt, " ") {
        return strings.Split(txt, " ")
    } else if strings.Contains(txt, ",") {
        return strings.Split(txt, ",")
    } else {
        count := 0
        for _, char := range txt {
            if char == 'a' || char == 'c' || char == 'e' || char == 'g' || char == 'i' || char == 'k' || char == 'l' || char == 'm' || char == 'o' || char == 'p' || char == 's' || char == 'u' || char == 'v' || char == 'x' || char == 'z' {
                if unicode.IsLower(char) {
                    count++
                }
            }
        }
        return count
    }
}
```

You can test the solution using the following code:

```go
func main() {
    fmt.Println(SplitWords("Hello world!")) // ["Hello", "world!"]
    fmt.Println(SplitWords("Hello,world!")) // ["Hello", "world!"]
    fmt.Println(SplitWords("abcdef"))       // 3
}
```

This will output:

```
[Hello world!]
[Hello world!]
3
```

Note that the solution assumes that