Here is the solution in Go:

```go
func Solve(s string) string {
    var letters []rune
    var nonLetters []rune
    
    for _, c := range s {
        if unicode.IsLetter(c) {
            letters = append(letters, unicode.ToLower(c))
        } else {
            nonLetters = append(nonLetters, c)
        }
    }
    
    if len(letters) > 0 {
        for i := 0; i < len(letters)/2; i++ {
            letters[i], letters[len(letters)-1-i] = letters[len(letters)-1-i], letters[i]
        }
        return string(nonLetters) + string(letters)
    }
    
    for i := 0; i < len(s)/2; i++ {
        s[i], s[len(s)-1-i] = s[len(s)-1-i], s[i]
    }
    
    return s
}
```

This function first separates the letters from the non-letters in the string. Then, if there are any letters, it reverses the order of the letters and concatenates them with the non-letters. If there are no letters, it simply reverses the entire string.

This solution assumes that the input string is a valid UTF-8 string. If the input string can contain invalid UTF-8 sequences, additional checks should be added to handle those cases.