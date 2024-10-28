    count := 0
    vowels := "aeiou"

    for _, letter := range strings.ToLower(s) {
        if strings.ContainsRune(vowels, letter) {
            count++
        }
    }

    if len(s) > 0 && s[len(s)-1] == 'y' {
        count++
    }

    return count
}

```

## Question 3

```go
