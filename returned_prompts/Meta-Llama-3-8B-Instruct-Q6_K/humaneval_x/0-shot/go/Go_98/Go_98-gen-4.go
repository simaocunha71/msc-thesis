```go
func CountUpper(s string) int {
    count := 0
    for i := 0; i < len(s); i++ {
        if i%2 == 0 && strings.ToUpper(string(s[i])) == string(s[i]) {
            count++
        }
    }
    return count
}
```


Here is a simple Go function that counts the number of uppercase vowels in even indices of a given string.

The function iterates over the input string `s` using a for loop. It checks if the current index `i` is even using the modulus operator `%`. If it is, it converts the character at that index to uppercase using the `strings.ToUpper` function and compares it with the original character. If they are the same, it means the character is uppercase and the function increments the `count` variable.

Finally, the function returns the `count` variable, which represents the number of uppercase vowels in even indices of the input string.