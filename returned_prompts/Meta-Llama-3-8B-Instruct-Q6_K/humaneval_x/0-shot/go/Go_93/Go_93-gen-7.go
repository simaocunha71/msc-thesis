Here is a possible implementation of the function:
```go
func Encode(message string) string {
    result := ""
    for _, r := range message {
        if unicode.IsLetter(r) {
            switch {
            case unicode.IsLower(r):
                result += string(unicode.ToUpper(r))
            case unicode.IsUpper(r):
                result += string(unicode.ToLower(r))
            }
            if r == 'a' || r == 'e' || r == 'i' || r == 'o' || r == 'u' {
                switch r {
                case 'a':
                    result += 'c'
                case 'e':
                    result += 'g'
                case 'i':
                    result += 'k'
                case 'o':
                    result += 'q'
                case 'u':
                    result += 'w'
                }
            } else {
                result += string(r)
            }
        } else {
            result += string(r)
        }
    }
    return result
}
```
This function iterates over each character in the input message. If the character is a letter, it checks if it is uppercase or lowercase and swaps its case accordingly. Then, it checks if the letter is a vowel (a, e, i, o, or u) and if so, replaces it with the letter that appears 2 places ahead of it in the alphabet. If the character is not a letter, it leaves it unchanged. Finally, it returns the encoded message.