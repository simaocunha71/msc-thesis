To decode a string that was encoded using the `EncodeShift` function, you need to perform the inverse operation. This involves shifting each character back by 5 positions in the alphabet. Here's how you can implement the `DecodeShift` function:

```go
func DecodeShift(s string) string {
    runes := []rune(s)
    newRunes := make([]rune, 0)
    for _, ch := range runes {
        newRunes = append(newRunes, (ch-5-'a')%26+'a')
    }
    return string(newRunes)
}
```

In this function, we iterate over each rune in the input string `s`. For each character, we subtract 5 from its Unicode code point (`ch`) and then add `'a'` to shift it back to the range of lowercase letters. We also use the modulo operation (`%26`) to ensure that the character wraps around within the alphabet when the subtraction goes negative. The result is then appended to a new slice of runes. Finally, we convert the slice back to a string and return it.