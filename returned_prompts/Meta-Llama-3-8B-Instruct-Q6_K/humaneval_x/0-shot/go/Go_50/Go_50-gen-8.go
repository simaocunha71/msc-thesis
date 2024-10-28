```go
func EncodeShift(s string) string {
    runes := []rune(s)
    newRunes := make([]rune, 0)
    for _, ch := range runes {
        if ch >= 'a' && ch <= 'z' {
            newRunes = append(newRunes, (ch+5-'a')%26+'a')
        } else if ch >= 'A' && ch <= 'Z' {
            newRunes = append(newRunes, (ch+5-'A')%26+'A')
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
        } else if ch >= 'A' && ch <= 'Z' {
            newRunes = append(newRunes, (ch-5-'A')%26+'A')
        } else {
            newRunes = append(newRunes, ch)
        }
    }
    return string(newRunes)
}
```



The provided code is incomplete and does not correctly implement the Caesar cipher. It seems to be missing the logic for handling non-alphabetic characters.

The corrected code for `EncodeShift` function should check if the character is a lowercase or uppercase letter and apply the shift accordingly. If the character is not a letter, it should be left unchanged.

Here is the corrected code:

```go
func EncodeShift(s string) string {
    runes := []rune(s)
    newRunes := make([]rune, 0)
    for _, ch := range runes {
        if ch >= 'a' && ch <= 'z' {
            newRunes = append(newRunes, (ch+5-'a')%26+'a')
        } else if ch >= 'A' && ch <= 'Z' {
            newRunes = append(newRunes, (ch+5-'A')%26+'A')
        } else {
            newRunes = append(newRunes, ch)
        }
    }
    return string(newRunes)
}
```

The `DecodeShift` function should work similarly,