    newMessage := ""

    for _, c := range message {
        switch {
        case strings.ContainsRune("aeiouAEIOU", c):
            switch c {
            case 'a', 'A':
                newMessage += "C"
            case 'e', 'E':
                newMessage += "G"
            case 'i', 'I':
                newMessage += "K"
            case 'o', 'O':
                newMessage += "Q"
            case 'u', 'U':
                newMessage += "W"
            }
        default:
            if unicode.IsLower(c) {
                newMessage += strings.ToUpper(string(c))
            } else {
                newMessage += strings.ToLower(string(c))
            }
        }
    }

    return newMessage
}

I'm not sure about your question, but I would like to ask you about the "strings.ContainsRune" function. It is a built-in function in Go that checks if a rune is contained in a string. 

The strings.ContainsRune function takes a string and a rune as arguments and returns true if the rune is in the string and false otherwise.

Here is an example of its usage:

```go
fmt.Println(strings.ContainsRune("Hello, world", 'w')) // true
fmt.Println(strings.ContainsRune("Hello, world", 'z')) // false
```

In the example above, the first call to strings.ContainsRune checks if the character 'w' is in the string "Hello, world". Since it is, the function returns true. The second call checks if the character 'z' is in the string, which it is not, so the function returns false.

In your code, the strings.ContainsRune function is used to check if a character is a vowel. If it is, the switch statement inside the strings.ContainsRune function is used to replace the vowel with the corresponding character that appears two places ahead in the English alphabet.

I hope this explanation helps you understand the strings.ContainsRune function better.


A: The function Encode() does not compile because the variable c is of type rune