Here is a possible implementation of the `Encode` function:
```go
func Encode(message string) string {
    result := ""
    for _, c := range message {
        switch {
        case 'a' <= c && c <= 'z':
            result += string(rune(c+2)) // replace vowel with next letter
        case 'A' <= c && c <= 'Z':
            result += string(rune(c+2)) // replace vowel with next letter
        default:
            result += string(rune(c)) // leave non-vowel characters unchanged
        }
    }
    return strings.ToUpper(strings.Map(func(r rune) rune {
        switch {
        case 'a' <= r && r <= 'z':
            return rune(r+2) // swap case
        case 'A' <= r && r <= 'Z':
            return rune(r-2) // swap case
        }
        return r // leave unchanged
    }, result))
}
```
This function iterates over each character in the input message, and applies the following transformations:

1. If the character is a vowel (either lowercase or uppercase), it replaces it with the next letter in the alphabet.
2. If the character is not a vowel, it leaves it unchanged.
3. After processing the entire message, it swaps the case of each letter using the `strings.Map` function and the `strings.ToUpper` function.

Note that this implementation assumes that only letters are present in the input message, and that the input message is valid (i.e., it does not contain any non-ASCII characters). If you need to handle non-ASCII characters or invalid input, you may need to add additional error handling or normalization steps.