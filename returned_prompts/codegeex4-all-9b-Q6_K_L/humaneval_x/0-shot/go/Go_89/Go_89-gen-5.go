Here is the solution for your problem:

```go
func Encrypt(s string) string {
    var result string
    for _, ch := range s {
        if ch >= 'a' && ch <= 'z' {
            result += string((ch-'a'+2*2)%26 + 'a')
        } else if ch >= 'A' && ch <= 'Z' {
            result += string((ch-'A'+2*2)%26 + 'A')
        } else {
            result += string(ch)
        }
    }
    return result
}
```
This function uses the ASCII values of the characters to shift them. For lower case letters, it starts from 'a' (which has an ASCII value of 97) and for upper case letters, it starts from 'A' (which has an ASCII value of 65). It then adds 4 (2*2) to the ASCII value of the character and takes the modulus 26 to ensure the result is still within the range of the alphabet. Finally, it converts the ASCII value back to a character and adds it to the result string.