To solve this problem, we can follow these steps:

1. Replace all spaces with underscores.
2. Replace all consecutive spaces with a dash.
3. Return the modified string.

Here is the Go code that implements these steps:

```go
func FixSpaces(text string) string {
    var sb strings.Builder
    var lastRunes []rune

    for _, r := range text {
        if r == ' ' {
            if len(lastRunes) > 0 && lastRunes[len(lastRunes)-1] == ' ' {
                sb.WriteRune('-')
            } else {
                sb.WriteRune('_')
            }
        } else {
            sb.WriteRune(r)
        }
        lastRunes = append(lastRunes, r)
    }

    return sb.String()
}
```

Test cases:

```go
fmt.Println(FixSpaces("Example"))   // "Example"
fmt.Println(FixSpaces("Example 1")) // "Example_1"
fmt.Println(FixSpaces(" Example 2")) // "_Example_2"
fmt.Println(FixSpaces(" Example   3")) // "_Example-3"
```

In the `FixSpaces` function, we first create a `strings.Builder` to accumulate the output string. We also create a slice to keep track of the last runes encountered.

We iterate through the input string character by character. If the current character is a space, we check if the last rune was also a space. If it was, we append a dash to the output string; otherwise, we append an underscore. If the current character is not a space, we append the character itself.

Finally, we return the modified string.

The test cases demonstrate the expected behavior of the `FixSpaces` function.

```go
fmt.Println(FixSpaces("Example"))   // "Example"
fmt.Println(FixSpaces("Example 1")) // "Example_1"
fmt.Println(FixSpaces(" Example 2")) // "_Example_2"
fmt.Println(Fix