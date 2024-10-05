Here is a simple solution to the problem using Go:

```go
func Encrypt(s string) string {
    runes := []rune(s)
    for i := range runes {
        runes[i] = (runes[i] - 'a' + 4) % 26 + 'a'
    }
    return string(runes)
}
```

This function first converts the string to a slice of runes, which allows us to manipulate individual characters. Then it iterates over the runes, shifting each one down by 4 places in the alphabet (equivalent to multiplying by two and adding two). The modulo operator is used to wrap around the alphabet if necessary. Finally, it converts the slice of runes back to a string and returns it.