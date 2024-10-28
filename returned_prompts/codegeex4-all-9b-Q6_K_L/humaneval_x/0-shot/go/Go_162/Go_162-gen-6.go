Here's how you can define the `StringToMd5` function in Go:

```go
import (
    "crypto/md5"
    "fmt"
)

func StringToMd5(text string) interface{} {
    if text == "" {
        return nil
    }

    hash := md5.Sum([]byte(text))
    return fmt.Sprintf("%x", hash)
}
```

This function first checks if the input string is empty. If it is, it returns `nil`. Otherwise, it creates an MD5 hash of the input string and returns it as a string. The `fmt.Sprintf("%x", hash)` part of the function is used to convert the MD5 hash into a hexadecimal string.