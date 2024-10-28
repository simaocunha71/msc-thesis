    var result string

B:
    for _, char := range str {
        if unicode.IsLower(char) {
            result += strings.ToUpper(string(char))
        } else {
            result += strings.ToLower(string(char))
        }
    }

C:
    return result
}

// >>> FlipCase('Hello')
// 'hELLO'
```

### Go 语言中的字符串拼接

在 Go 语言中，使用 `+` 进行字符串拼接，如果需要拼接的字符串数量很多，效率可能会降低。Go 语言提供了 `strings.Builder` 来提高字符串拼接的效率。

```go
