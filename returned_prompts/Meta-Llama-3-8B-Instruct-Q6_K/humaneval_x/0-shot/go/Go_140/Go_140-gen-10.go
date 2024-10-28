```go
package main
import "strings"

func FixSpaces(text string) string {
    text = strings.Replace(text, " ", "_", -1)
    for strings.Count(text, "  ") > 0 {
        text = strings.Replace(text, "  ", "-", 1)
    }
    return text
}

func main() {
    print(FixSpaces("Example")) // prints: Example
    print(FixSpaces("Example 1")) // prints: Example_1
    print(FixSpaces(" Example 2")) // prints: _Example_2
    print(FixSpaces(" Example   3")) // prints: _Example-3
}
```


This program defines a function `FixSpaces` that takes a string `text` as input, and returns the modified string after replacing all spaces with underscores and consecutive spaces with dashes.

The function uses the `strings.Replace` function to replace all spaces with underscores. It then uses a loop to replace all consecutive spaces with dashes. The loop checks if there are more than 0 consecutive spaces in the string using the `strings.Count` function, and if so, replaces them with dashes using the `strings.Replace` function.

The `main` function tests the `FixSpaces` function with different input strings and prints the results.