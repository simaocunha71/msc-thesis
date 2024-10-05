You can use the same logic as in the EncodeShift function, but instead of adding 5 to each character, you need to subtract 5. Here is the corrected DecodeShift function:

```
func DecodeShift(s string) string {
    runes := []rune(s)
    newRunes := make([]rune, 0)
    for _, ch := range runes {
        newRunes = append(newRunes, (ch-5-'a')%26+'a')
    }
    return string(runes)
}
```