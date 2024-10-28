Here is the solution in Go:
```go
import (
    "crypto/md5"
    "fmt"
    "encoding/hex"
)

// Given a string 'text', return its md5 hash equivalent string.
// If 'text' is an empty string, return nil.
func StringToMd5(text string) interface{} {
    if text == "" {
        return nil
    }
    hash := md5.New()
    hash.Write([]byte(text))
    md5Bytes := hash.Sum(nil)
    return hex.EncodeToString(md5Bytes[:])
}

func main() {
    fmt.Println(StringToMd5("Hello world")) // Output: 3e25960a79dbc69b674cd4ec67a72c62
}
```
This function takes a string as input and returns its MD5 hash equivalent string. If the input string is empty, it returns `nil`. It uses the `md5` package to calculate the hash and the `hex` package to encode the hash bytes as a hexadecimal string.

In the `main` function, we test the `StringToMd5` function with the input string "Hello world" and print the result. The output is the MD5 hash of the input string, which is "3e25960a79dbc69b674cd4ec67a72c62".