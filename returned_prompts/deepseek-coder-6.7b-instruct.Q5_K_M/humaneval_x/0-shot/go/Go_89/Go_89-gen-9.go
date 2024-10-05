    var result string
    for _, char := range s {
        switch {
        case char >= 'a' && char <= 'z':
            result += string((char-'a'+2*2)%26 + 'a')
        case char >= 'A' && char <= 'Z':
            result += string((char-'A'+2*2)%26 + 'A')
        default:
            result += string(char)
        }
    }
    return result
}
```

## 1.2.4. 解密函数

创建一个函数来解密加密的字符串。

```go
