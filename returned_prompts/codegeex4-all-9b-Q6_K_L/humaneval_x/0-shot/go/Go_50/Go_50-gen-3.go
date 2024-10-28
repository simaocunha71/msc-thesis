The `EncodeShift` function is encoding a string by shifting every character by 5 in the alphabet. The `DecodeShift` function should take as input a string encoded with `EncodeShift` and return the decoded string.

Here's how you can implement the `DecodeShift` function:

```go
func DecodeShift(s string) string {
    runes := []rune(s)
    newRunes := make([]rune, 0)
    for _, ch := range runes {
        newRunes = append(newRunes, (ch-5-'a')%26+'a')
    }
    return string(runes)
}
```

The `DecodeShift` function works similarly to the `EncodeShift` function, but it shifts the characters in the opposite direction. Instead of adding 5 to the character's ASCII value, it subtracts 5. The rest of the logic is the same, so the characters are shifted back to their original positions, effectively decoding the string.