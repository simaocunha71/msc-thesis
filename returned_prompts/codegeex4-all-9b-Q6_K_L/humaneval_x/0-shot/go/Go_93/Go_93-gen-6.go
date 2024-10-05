Here's how you might do it in Go:

```go
func Encode(message string) string {
    vowels := "aeiou"
    encoded := ""
    for _, char := range message {
        if strings.ContainsRune(vowels, char) {
            encoded += string(char + 2)
        } else {
            if 'a' <= char && char <= 'z' {
                encoded += string(char - 32)
            } else if 'A' <= char && char <= 'Z' {
                encoded += string(char + 32)
            } else {
                encoded += string(char)
            }
        }
    }
    return encoded
}
```
This function iterates over each character in the input string. If the character is a vowel, it adds the character that comes two places later in the alphabet. If the character is a lower case letter, it converts it to upper case, if it's an upper case letter, it converts it to lower case, and if it's neither a letter nor a vowel, it leaves it as it is. The result is a string where all letters have had their case swapped and all vowels have been replaced by the letter two places ahead in the alphabet.

Please note that this function assumes that the input string only contains English letters and does not handle non-English characters.