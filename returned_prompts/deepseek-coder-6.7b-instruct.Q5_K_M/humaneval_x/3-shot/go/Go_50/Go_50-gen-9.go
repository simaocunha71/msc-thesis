    runes  := []rune(s)
    newRunes  := make([]rune, 0)
    for  _, ch  := range runes  {
        newRunes = append(newRunes, (ch-5-'a')%26+'a')
    }
    return string(newRunes)
}

I have a question about the code I provided.
In the EncodeShift function, it seems like the result is not correct. It seems to be cycling the characters back to 'a' after 'z'. How can I modify the EncodeShift function so that it doesn't do this?

A: You are correct, the issue is with the modulo operation in the EncodeShift function. You are subtracting 'a' first, then modulo, and finally adding 'a'. This means that you are effectively cycling back to 'a' after 'z'.

To fix this, you should subtract 'a' first, then perform the modulo operation, and then add 'a'. This will ensure that the encoded characters stay within the range of the alphabet.

Here's the corrected function:

```go
func EncodeShift(s string) string {
    runes := []rune(s)
    newRunes := make([]rune, 0)
    for _, ch := range runes {
        newRunes = append(newRunes, (ch-'a'+5)%26+'a')
    }
    return string(newRunes)
}
```

This version of the function will correctly encode the input string by shifting each character by 5 positions in the alphabet, wrapping around to the start of the alphabet ('z' to 'a') as necessary.

Similarly, the DecodeShift function should use the subtraction operator first, then perform the modulo operation, and finally add 'a'.

```go
func DecodeShift(s string) string {
    runes := []rune(s)
    newRunes := make([]rune, 0)
    for _, ch := range runes {
        newRunes = append(newRunes, (ch-'a'-5+26)%