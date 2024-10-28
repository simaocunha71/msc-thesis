    // Initialize result as the original string
    result := s

    // Loop over all characters in c
    for _, ch := range c {
        // Replace all occurrences of ch in result with nothing
        result = strings.ReplaceAll(result, string(ch), "")
    }

    // Check if the result string is a palindrome
    isPalindrome := result == Reverse(result)

    return [2]interface{}{result, isPalindrome}
}

func Reverse(s string) string {
    runes := []rune(s)
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}

```

I:
```go
func ReverseDelete(s,c string)  (string, bool) {
    result := strings.Map(func(r rune) rune {
        if strings.ContainsRune(c, r) {
            return -1
        }
        return r
    }, s)

    return result, result == Reverse(result)
}

func Reverse(s string) string {
    runes := []rune(s)
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}
```

```go
// Here I've used the strings.Map function to replace all characters in s that are in c with nothing (-1).
// Then I just check if the result string is a palindrome by comparing it to its reverse.
```

```go
// I've also used the strings.ContainsRune function to check if a character from s is in c.
// If it is, I return -1 to replace it with nothing.
```

```go
// This solution