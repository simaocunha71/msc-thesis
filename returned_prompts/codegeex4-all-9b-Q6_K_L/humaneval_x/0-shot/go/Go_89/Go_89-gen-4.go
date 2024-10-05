Here is a Go function that accomplishes this:

```go
func Encrypt(s string) string {
    const alphabet = "abcdefghijklmnopqrstuvwxyz"
    var encrypted string
    for _, char := range s {
        index := strings.Index(alphabet, string(char))
        if index == -1 {
            encrypted += string(char)
        } else {
            newChar := alphabet[(index+4)%len(alphabet)]
            encrypted += string(newChar)
        }
    }
    return encrypted
}
```

In this function, we first define the alphabet. Then we loop over each character in the input string. If the character is not in the alphabet, we add it to the encrypted string as it is. If the character is in the alphabet, we find its index in the alphabet and rotate it by two places. The rotation is calculated by adding 4 to the index and taking the modulus of the length of the alphabet. We then add the new character to the encrypted string. Finally, we return the encrypted string.