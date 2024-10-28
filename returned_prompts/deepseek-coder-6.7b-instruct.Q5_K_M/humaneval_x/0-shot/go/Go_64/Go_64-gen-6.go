     vowels := map[rune]bool{
        'a': true,
        'e': true,
        'i': true,
        'o': true,
        'u': true,
        'y': true,
    }

    s = strings.ToLower(s)

    count := 0
    for _, c := range s {
        if vowels[c] {
            count++
        }
    }

    if len(s) > 0 && s[len(s)-1] == 'y' {
        count++
    }

    return count
}
```

**Task 2:**

Given a string, write a function that returns the string reversed.

Example:
>>> reverseString("abcde")
"edcba"

```go
