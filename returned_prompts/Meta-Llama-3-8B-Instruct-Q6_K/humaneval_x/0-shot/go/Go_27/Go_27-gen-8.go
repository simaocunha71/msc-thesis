Here is the solution in Go:

```go
import (
    "strings"
)

// FlipCase takes a string as input and returns the string with lowercase characters converted to uppercase and uppercase characters converted to lowercase.
func FlipCase(str string) string {
    runes := []rune(str)
    flipped := make([]rune, len(runes))
    for i, runeVal := range runes {
        if strings.ToLower(string(runeVal)) == string(runeVal) {
            flipped[i] = strings.ToUpper(string(runeVal))
        } else {
            flipped[i] = strings.ToLower(string(runeVal))
        }
    }
    return string(flipped)
}
```

You can call this function with a string as an argument and it will return the flipped string. For example:

```go
result := FlipCase("Hello")
fmt.Println(result) // Output: "hELLO"
```


This function works by first converting the input string into a slice of runes. Then it creates a new slice of runes to store the flipped characters. It iterates over the original slice of runes, checks if the character is lowercase or uppercase using the `strings.ToLower` and `strings.ToUpper` functions, and flips the character accordingly. Finally, it converts the flipped slice of runes back into a string and returns it.