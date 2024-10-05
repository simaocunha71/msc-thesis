```go
func FixSpaces(text string) string {
    var sb strings.Builder
    var prevRune rune
    for _, c := range text {
        if c == ' ' {
            if prevRune == ' ' {
                if sb.Len() > 0 {
                    sb.WriteString("-")
                }
            } else {
                sb.WriteString("_")
            }
        } else {
            sb.WriteString(string(c))
        }
        prevRune = c
    }
    return sb.String()
}
```


The function takes a string as an input, and then iterates over the string character by character. For each character, it checks if it's a space. If it is, it checks if the previous character was also a space. If it was, it adds a hyphen to the result string. If it wasn't, it adds an underscore. If the character is not a space, it simply adds it to the result string. The function returns the result string at the end. This way, all spaces are replaced with underscores, and consecutive spaces are replaced with hyphens.