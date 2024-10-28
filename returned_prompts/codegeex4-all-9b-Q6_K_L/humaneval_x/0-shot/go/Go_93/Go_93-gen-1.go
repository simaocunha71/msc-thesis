Here is a simple solution in Go:

```go
func Encode(message string) string {
    vowels := "aeiou"
    result := ""
    for _, char := range message {
        if strings.ContainsRune(vowels, char) {
            result += string(char - 32)
        } else if char >= 65 && char <= 90 {
            result += string(char + 32)
        } else if char >= 97 && char <= 122 {
            result += string(char - 32)
        } else {
            result += string(char)
        }
    }
    return result
}
```
This function iterates over each character in the message. If the character is a vowel, it converts it to uppercase. If the character is uppercase, it converts it to lowercase. If the character is lowercase, it converts it to uppercase. If the character is not a vowel, it leaves it unchanged.