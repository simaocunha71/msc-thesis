Here is the solution in Go:
```go
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
    md5sum := hash.Sum(nil)
    return hex.EncodeToString(md5sum[:])
}
```
Here's an explanation of the code:

1. We import the `crypto/md5` package to use the MD5 hash function, `encoding/hex` to encode the hash as a hexadecimal string, and `fmt` for printing.
2. We define the `StringToMd5` function, which takes a string `text` as input.
3. We check if the input string is empty. If it is, we return `nil`.
4. We create a new MD5 hash object using `md5.New()`.
5. We write the input string to the hash object using `hash.Write([]byte(text))`.
6. We calculate the MD5 hash by calling `hash.Sum(nil)`, which returns the hash as a byte slice.
7. We encode the hash as a hexadecimal string using `hex.EncodeToString(md5sum[:])`, where `md5sum` is the byte slice.
8. We return the encoded string.

You can test this function with the input `'Hello world'` to get the expected output `'3e25960a79dbc69b674cd4ec67a72c62'`. If you pass an empty string, the function will return `nil`.