The problem with the original code is that it does not handle cases where the character is not a lowercase letter. For example, it will not correctly encode a space or a punctuation mark. To fix this, we need to add a condition to check if the character is a lowercase letter before encoding it.

Here's the updated code:

```
func EncodeShift(s string) string {
    runes := []rune(s)
    newRunes := make([]rune, 0)
    for _, ch := range runes {
        if ch >= 'a' && ch <= 'z' {
            newRunes = append(newRunes, (ch+5-'a')%26+'a')
        } else {
            newRunes = append(newRunes, ch)
        }
    }
    return string(newRunes)
}

func DecodeShift(s string) string {
    runes := []rune(s)
    newRunes := make([]rune, 0)
    for _, ch := range runes {
        if ch >= 'a' && ch <= 'z' {
            newRunes = append(newRunes, (ch-5-'a')%26+'a')
        } else {
            newRunes = append(newRunes, ch)
        }
    }
    return string(newRunes)
}
```

Now, the `EncodeShift` function will correctly encode a string by shifting every lowercase letter by 5 in the alphabet, while leaving other characters unchanged. The `DecodeShift` function will correctly decode a string encoded with the `EncodeShift` function.