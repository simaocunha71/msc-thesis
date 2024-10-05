    return strings.FieldsFunc(s, func(c rune) bool {
        return c == ',' || c == ' '
    })
}

// We use the FieldsFunc function from the strings package to split the string into
// words. The function takes a string and a function that decides where the string
// should be split. Here, we use it to split the string on either a comma or a
// space, and return the resulting slice of words.
```

### 解法二：使用正则表达式

```go
