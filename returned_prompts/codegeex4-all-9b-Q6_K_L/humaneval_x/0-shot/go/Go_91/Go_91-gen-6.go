Here's the solution. This function uses regular expressions to find all the sentences that start with the word "I" and count them:

```go
func IsBored(S string) int {
    re := regexp.MustCompile(`(?i)^[iI]\b.*?[.!?]\s`)
    return len(re.FindAllString(S, -1))
}
```

This function uses the `regexp.MustCompile` function to compile a regular expression. The regular expression looks for the start of a string (^), followed by the word "I" or "i" (due to the `(?i)` flag), followed by any number of characters (due to `.*?`), followed by a period, question mark, or exclamation mark (due to `[.!?]`), followed by a space (due to `\s`). This regular expression is case-insensitive due to the `(?i)` flag.

The `FindAllString` function is then used to find all the substrings in `S` that match the regular expression. The length of these substrings is then returned, which is the number of boredoms.