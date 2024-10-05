    words := strings.Fields(s)
    for i, word := range words {
        chars := []rune(word)
        sort.Slice(chars, func(i, j int) bool {
            return chars[i] < chars[j]
        })
        words[i] = string(chars)
    }
    return strings.Join(words, " ")
}
```

## 4. 
```go
