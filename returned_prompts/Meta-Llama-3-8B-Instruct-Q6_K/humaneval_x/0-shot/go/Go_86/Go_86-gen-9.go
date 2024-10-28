Here is the solution in Go programming language:

```go
package main

import (
    "fmt"
    "sort"
    "strings"
)

func antiShuffle(s string) string {
    words := strings.Split(s, " ")
    result := make([]string, len(words))
    for i, word := range words {
        runes := []rune(word)
        sort.Runes(runes)
        result[i] = string(runes)
    }
    return strings.Join(result, " ")
}

func main() {
    fmt.Println(antiShuffle("Hi"))  // Output: "Hi"
    fmt.Println(antiShuffle("hello"))  // Output: "ehllo"
    fmt.Println(antiShuffle("Hello World!!!"))  // Output: "!!!Hello Wdlor"
}
```

Explanation:
The function `antiShuffle` takes a string as input and returns a new string where all words are replaced by a new word where all the characters are arranged in ascending order based on ASCII value.

1. The input string is split into individual words using the `strings.Split` function.
2. For each word, the characters are converted to a slice of runes using the `[]rune` syntax.
3. The `sort.Runes` function is used to sort the runes in ascending order.
4. The sorted runes are then converted back to a string using the `string` function.
5. The resulting strings are joined back together with spaces using the `strings.Join` function.

The `main` function demonstrates the usage of the `antiShuffle` function with different inputs. The output for each input is printed to the console.