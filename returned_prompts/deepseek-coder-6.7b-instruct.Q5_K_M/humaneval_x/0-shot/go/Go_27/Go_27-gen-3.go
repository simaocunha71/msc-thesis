The above code is correct but it does not consider characters that are not letters (like digits, symbols, whitespace, etc.). We can modify the code to handle these characters directly without converting them to strings first:

```go
import (
    "unicode"
)

func FlipCase(str string) string {
    flipped := []rune(str)
    for i, c := range flipped {
        if unicode.IsLower(c) {
            flipped[i] = unicode.ToUpper(c)
        } else if unicode.IsUpper(c) {
            flipped[i] = unicode.ToLower(c)
        }
    }
    return string(flipped)
}
```

This code works by creating a slice of runes (which are the Go equivalent of characters) from the input string. It then iterates over the runes, flipping them if they are lowercase or uppercase, and replaces the original rune in the slice. Finally, it converts the slice of runes back to a string and returns it.

Note: The above function will not work correctly with characters outside of the Basic Multilingual Plane (BMP), i.e., those characters that are represented by more than one UTF-16 code unit. If you need to handle such characters, you'll need to use a different approach.

```go
import (
    "unicode"
)

func FlipCase(str string) string {
    flipped := []rune(str)
    for i, c := range flipped {
        if unicode.IsLower(c) {
            flipped[i] = unicode.ToUpper(c)
        } else if unicode.IsUpper(c) {
            flipped[i] = unicode.ToLower