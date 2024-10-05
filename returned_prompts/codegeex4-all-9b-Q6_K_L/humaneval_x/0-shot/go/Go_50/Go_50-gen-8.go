To decode a string that was encoded with the `EncodeShift` function, you need to shift each character back by 5 positions in the alphabet. Here's how you can implement the `DecodeShift` function:

```go
// takes as input string encoded with EncodeShift function. Returns decoded string.
func DecodeShift(s string) string {
    runes := []rune(s)
    newRunes := make([]rune, 0)
    for _, ch := range runes {
        newRunes = append(newRunes, (ch-5-'a')%26+'a')
    }
    return string(newRunes)
}
```

In this function, we iterate over each character in the input string, which is represented as a slice of runes. For each rune, we subtract 5 from its Unicode value, then adjust it to be within the range of lowercase letters ('a' to 'z') by taking the modulus of 26 and adding 'a'. This effectively shifts the character back by 5 positions in the alphabet. The resulting runes are then converted back into a string and returned.