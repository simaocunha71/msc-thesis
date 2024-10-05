    vowels := "aeiouAEIOU"
    if i := bytes.IndexByte(word, 'a'); i > 0 && i < len(word)-1 && vowels[0] != word[i] && vowels[len(vowels)-1] != word[i] {
        return string(word[i])
    }
    if i := bytes.IndexByte(word, 'e'); i > 0 && i < len(word)-1 && vowels[1] != word[i] && vowels[len(vowels)-1] != word[i] {
        return string(word[i])
    }
    if i := bytes.IndexByte(word, 'i'); i > 0 && i < len(word)-1 && vowels[2] != word[i] && vowels[len(vowels)-1] != word[i] {
        return string(word[i])
    }
    if i := bytes.IndexByte(word, 'o'); i > 0 && i < len(word)-1 && vowels[3] != word[i] && vowels[len(vowels)-1] != word[i] {
        return string(word[i])
    }
    if i := bytes.IndexByte(word, 'u'); i > 0 && i < len(word)-1 && vowels[4] != word[i] && vowels[len(vowels)-1] != word[i] {
        return string(word[i])
    }
    return ""



























```
```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```