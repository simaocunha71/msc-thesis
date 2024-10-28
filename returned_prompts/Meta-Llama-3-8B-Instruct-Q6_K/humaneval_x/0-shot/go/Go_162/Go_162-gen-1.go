```go
package main

import (
    "crypto/md5"
    "fmt"
    "encoding/hex"
)

func StringToMd5(text string) interface{} {
    if text == "" {
        return nil
    }
    hash := md5.New()
    hash.Write([]byte(text))
    digest := hash.Sum(nil)
    return fmt.Sprintf("%x", hex.EncodeToString(digest))
}

func main() {
    fmt.Println(StringToMd5("Hello world")) // Output: 3e25960a79dbc69b674cd4ec67a72c62
}
```
In this solution, we are using the `crypto/md5` package to calculate the MD5 hash of the input string. We first create a new MD5 hash object using `md5.New()`. Then we write the input string to the hash object using `hash.Write([]byte(text))`. Finally, we get the hash digest using `hash.Sum(nil)` and encode it to a hexadecimal string using `hex.EncodeToString(digest)`. We then return this hexadecimal string.

If the input string is empty, we return `nil`. This is because the problem statement asks for the MD5 hash equivalent string, but an empty string doesn't have an MD5 hash equivalent string. Instead, we return `nil` to indicate that the input string is empty.