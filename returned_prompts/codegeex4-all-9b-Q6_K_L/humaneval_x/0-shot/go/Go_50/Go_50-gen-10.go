The DecodeShift function can be implemented in a similar way to the EncodeShift function. The only difference is that instead of adding 5 to the character, we need to subtract 5. Here's the updated code:

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

In this code, we subtract 5 from the character, convert it to a rune, and append it to the newRunes slice. Finally, we return the string representation of the newRunes slice.