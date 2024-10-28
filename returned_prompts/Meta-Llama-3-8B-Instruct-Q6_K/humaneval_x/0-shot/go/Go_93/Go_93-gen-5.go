Here is the Go function that implements the described encoding:

```go
func Encode(message string) string {
    result := ""
    for _, char := range message {
        if char >= 'a' && char <= 'z' {
            if char == 'a' || char == 'e' || char == 'i' || char == 'o' || char == 'u' {
                result += string(rune(char + 2))
            } else {
                result += string(rune(char + 1))
            }
        } else if char >= 'A' && char <= 'Z' {
            if char == 'A' || char == 'E' || char == 'I' || char == 'O' || char == 'U' {
                result += string(rune(char + 2))
            } else {
                result += string(rune(char + 1))
            }
        } else {
            result += string(char)
        }
    }
    return strings.ToUpper(result)
}
```

This function iterates over each character in the input message. If the character is a lowercase or uppercase letter, it checks if it is a vowel. If it is, it replaces the vowel with the letter that appears 2 places ahead of it in the English alphabet. If it is not a vowel, it simply increments the ASCII value of the character by 1. If the character is not a letter, it leaves it unchanged. Finally, it converts the result to uppercase using the `strings.ToUpper` function. This is because the problem statement asks to "swap case of all letters", which means converting all lowercase letters to uppercase and vice versa. The `strings.ToUpper` function achieves this by converting all letters to uppercase. 