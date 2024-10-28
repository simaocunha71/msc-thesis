To solve this problem, we can use the `strings` package from the Go standard library. This package provides a function called `Fields` which splits a string into a slice of substrings using whitespace and newlines as delimiters. If no delimiter is provided, `Fields` uses whitespace.

Here's a step-by-step breakdown of the solution:

1. Import the `strings` package: `import "strings"`
2. Define the `SplitWords` function that takes a string `txt` as input.
3. Use the `Fields` function from the `strings` package to split the `txt` string into a slice of substrings. Store the result in a variable called `words`.
4. Check if the `words` slice is empty. If it is, it means that there were no whitespaces or commas in the `txt` string. In this case, initialize a variable called `count` to 0 and iterate over each character in the `txt` string. For each character, check if it is a lowercase letter and if its ordinal value (`ord`) is odd. If both conditions are true, increment the `count` variable. Finally, return the `count` variable.
5. If the `words` slice is not empty, it means that the `txt` string was split successfully. In this case, return the `words` slice.
6. To test the `SplitWords` function, use the `fmt.Println` function to print the result of the function with different test cases.

Here's an example of how to use the `SplitWords` function:

```go
package main

import (
    "fmt"
    "strings"
)

func SplitWords(txt string) interface{} {
    words := strings.Fields(txt)
    if len(words) == 0 {
        count := 0
        for _, c := range txt {
            if 'a' <= c && c <= 'z' && (c-'a')%2 == 1 {
                count++
            }
        }
        return count
    }
    return words
}

func main() {
    fmt.Println(SplitWords("Hello world!")) // ["Hello", "world!"]
    fmt.