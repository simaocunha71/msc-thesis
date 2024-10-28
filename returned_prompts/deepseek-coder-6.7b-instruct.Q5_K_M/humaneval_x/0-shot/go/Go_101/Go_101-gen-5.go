    return strings.FieldsFunc(s, func(r rune) bool {
        return !strings.In(r, " ,.")
    })
}

The strings.FieldsFunc function is used to split the string into words. It splits the string at every rune that is not a comma, space, or period. 

The strings.In function is used to check if a rune is not a comma, space, or period. If a rune is not one of these characters, it is considered a delimiter and the string is split at this point. The resulting substrings are the words of the string.

This solution assumes that words are separated by a space, a comma, or a period, and that there are no multiple spaces between words. It also assumes that words contain no spaces within them.

Please note that the strings.In function does not exist in the Go standard library, it's a hypothetical function that might be in your own codebase. In the actual code, you would use the equality operator to check if a rune is not one of the characters in a string.

Here's how you could implement such a function:

```go
func notIn(r rune, s string) bool {
    for _, rune := range s {
        if r == rune {
            return false
        }
    }
    return true
}
```

And here's how you could use it in your code:

```go
func WordsString(s string) []string {
    return strings.FieldsFunc(s, func(r rune) bool {
        return !notIn(r, " ,.")
    })
}
```

This code will work the same way as the original code, but it uses the notIn function instead of strings.In.
