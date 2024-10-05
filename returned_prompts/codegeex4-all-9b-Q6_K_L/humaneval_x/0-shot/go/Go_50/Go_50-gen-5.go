The problem here is that in the DecodeShift function, you are using the wrong rune slice, so you are not actually decoding the string. You need to use the newRunes slice instead of runes. Here's the corrected code:

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

In this corrected version, we are using the newRunes slice to store the decoded characters, and then converting it back to a string before returning it.