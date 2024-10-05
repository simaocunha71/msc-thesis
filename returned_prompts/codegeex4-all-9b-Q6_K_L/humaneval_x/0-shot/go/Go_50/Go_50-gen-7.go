The EncodeShift function shifts every character in the input string by 5 positions in the alphabet. To decode the string, you need to shift it back by 5 positions. Here's the corrected DecodeShift function:

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

In the DecodeShift function, we subtract 5 from the character code and then add 'a' to get the original character code. The '%' operator is used to handle the wrap-around when the character code goes below 'a'.