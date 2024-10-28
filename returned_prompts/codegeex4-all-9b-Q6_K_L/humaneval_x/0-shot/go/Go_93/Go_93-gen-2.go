Here is a solution in Go:

```go
func Encode(message string) string {
    vowels := "aeiouAEIOU"
    result := ""
    for _, c := range message {
        if strings.ContainsRune(vowels, c) {
            result += string(c + 2)
        } else {
            if c >= 'a' && c <= 'z' {
                result += string(c - 32)
            } else if c >= 'A' && c <= 'Z' {
                result += string(c + 32)
            } else {
                result += string(c)
            }
        }
    }
    return result
}
```
This function loops through each character in the input string. If the character is a vowel (both lower-case and upper-case vowels are considered), it replaces the vowel with the vowel 2 places ahead in the alphabet. If the character is a letter (either lower-case or upper-case), it swaps its case. If the character is neither a vowel nor a letter (like a space or a punctuation mark), it leaves the character unchanged.

Please note that this solution assumes that the input string is in English and only contains letters, spaces, and punctuation marks. It does not handle other languages or special characters.