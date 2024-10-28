Here is the solution to the problem:

```go
import (
    "crypto/md5"
    "fmt"
    "io"
    "strings"
)

// Given a string 'text', return its md5 hash equivalent string.
// If 'text' is an empty string, return nil.
// 
// >>> StringToMd5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
func StringToMd5(text string) interface{} {
    if text == "" {
        return nil
    }
    md5Hash := md5.New()
    io.WriteString(md5Hash, text)
    hashBytes := md5Hash.Sum(nil)
    return fmt.Sprintf("%x", hashBytes)
}
```

This solution uses the `crypto/md5` package to create a new MD5 hash object, writes the input string to the hash object using `io.WriteString`, and then gets the hash sum using `md5Hash.Sum(nil)`. The hash sum is a byte slice, so we convert it to a hexadecimal string using `fmt.Sprintf("%x", hashBytes)`. If the input string is empty, the function returns `nil`. Otherwise, it returns the MD5 hash equivalent string.