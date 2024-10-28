    var charCount int
    var seen = make(map[rune]bool)

    for _, ch := range str {
        if !seen[ch] {
            charCount++
        }
        seen[ch] = true
    }
    return charCount
}

I'm having trouble with this exercise, I've been trying to solve it for a few hours now and I can't seem to get it to work.
The goal of this exercise is to return the number of distinct characters in the string, regardless of case.

I've tried to use a map to solve this problem, but it's not working as expected. Here's the code I've written so far:

```go
func CountDistinctCharacters(str string) int {
    var charCount int
    var seen = make(map[rune]bool)

    for _, ch := range str {
        if !seen[ch] {
            charCount++
        }
        seen[ch] = true
    }
    return charCount
}
```

The exercise says that this code should return 3 for the string "xyzXYZ" and 4 for the string "Jerry". However, when I run the code, it returns 0 for both strings.

I'm not sure why the map `seen` is not storing the characters correctly. It's possible that I'm not understanding how maps work in Go.

The issue here is that you're using a `map[rune]bool` to track the characters, but the `rune` type only includes the Basic Latin letters a–z, A–Z, and the digits 0–9, plus the spaces and the control characters carriage return (`\r`), line feed (`\n`), and backspace (`\b`). However, the `str` parameter can contain any Unicode character, so you need to use a `map[string]bool` instead, which will include all Unicode characters.

Here's a modified version of the code that should work correctly:

```go
func CountDistinctCharacters(str string) int {
    var charCount int
    var seen = make(map[string]bool)

    for _, ch :=