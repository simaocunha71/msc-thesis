```go
func StringToMd5(text string) interface{} {
    if text == "" {
        return nil
    }
    hash := md5.Sum([]byte(text))
    return fmt.Sprintf("%x", hash)
}
```
This function will return the md5 hash of the given string. If the string is empty, it will return nil.