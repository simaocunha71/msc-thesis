    runes  := []rune(s)
    newRunes  := make([]rune, 0)
    for _, ch  := range runes  {
        newRunes = append(newRunes, (ch-5-'a')%26+'a')
    }
    return string(newRunes)
}
```

In this code, `EncodeShift` shifts every character in the string by 5 places in the alphabet and `DecodeShift` does the opposite. `%26` ensures that we stay within the alphabet bounds.

Usage:

```go
func main() {
    s := "hello"
    encoded := EncodeShift(s)
    fmt.Println(encoded)  // "mjqqt"
    decoded := DecodeShift(encoded)
    fmt.Println(decoded)  // "hello"
}
```

You can see that `EncodeShift(s)` returns the string "mjqqt" and `DecodeShift(encoded)` returns the original string "hello".

**Note**: This code assumes that the input string only contains lowercase letters. If the input string can contain uppercase letters, you should add additional code to handle those cases.

**Note**: This code uses the ASCII values of the characters to perform the shift. In a Unicode-compatible language like Go, this could be a problem if the string contains characters outside of the ASCII range.

**Note**: The Caesar cipher is not secure for encrypting sensitive information. It is used as an example of a simple encryption technique for educational purposes.

**Note**: This code does not handle non-alphabetic characters correctly. It will shift them by 5 places in the alphabet, which is not what you want for punctuation and whitespace. You should add additional code to handle those cases.

**Note**: The shift of 5 is arbitrary and can be changed. The key is that the same shift must be used for encoding and decoding.

**Note**: The `%26` in the `%26+'a'` expression ensures that we stay within the alphabet bounds. If we don't do this, we could