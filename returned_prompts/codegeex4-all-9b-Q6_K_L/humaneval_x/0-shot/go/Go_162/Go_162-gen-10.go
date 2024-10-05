```go
func StringToMd5(text string) interface{} {
    if text == "" {
        return nil
    }

    hash := md5.Sum([]byte(text))
    return fmt.Sprintf("%x", hash)
}
```

