Here is the solution:

```go
func Encrypt(s string) string {
    alphabet := "abcdefghijklmnopqrstuvwxyz"
    result := ""
    for _, c := range s {
        if c >= 'a' && c <= 'z' {
            index := strings.IndexRune(alphabet, c)
            new_index := (index + 4) % len(alphabet)
            result += string(alphabet[new_index])
        } else {
            result += string(c)
        }
    }
    return result
}
```

Explanation:
The function `Encrypt` takes a string `s` as an argument and returns an encrypted string. The encryption works by rotating the alphabet by 4 places. The function iterates over each character `c` in the string. If the character is a lowercase letter, it finds its index in the alphabet, adds 4 to it (wrapping around to the beginning of the alphabet if necessary), and uses this new index to get the corresponding character from the alphabet. If the character is not a lowercase letter, it is left unchanged. The encrypted characters are concatenated to form the result string. The `strings.IndexRune` function is used to find the index of a character in a string, and the `%` operator is used for wrapping around the alphabet. The `string(alphabet[new_index])` expression is used to convert the character at the new index back into a string. The function returns the encrypted string.