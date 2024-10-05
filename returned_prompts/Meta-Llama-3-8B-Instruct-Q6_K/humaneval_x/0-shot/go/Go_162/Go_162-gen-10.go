Here is a possible solution in Go:
```go
import (
    "crypto/md5"
    "encoding/hex"
    "fmt"
)

func StringToMd5(text string) interface{} {
    if text == "" {
        return nil
    }
    hash := md5.New()
    hash.Write([]byte(text))
    digest := hash.Sum(nil)
    return hex.EncodeToString(digest[:])
}
```
Here's an explanation of the code:

1. We import the `crypto/md5` package for MD5 hashing, `encoding/hex` for converting the hash to a hexadecimal string, and `fmt` for printing.
2. We define the `StringToMd5` function, which takes a `string` argument `text`.
3. We check if `text` is an empty string. If it is, we return `nil`.
4. We create a new MD5 hash object using `md5.New()`.
5. We write the input `text` to the hash object using `hash.Write()`.
6. We get the hash digest using `hash.Sum(nil)`, which returns the hash as a byte slice.
7. We convert the hash digest to a hexadecimal string using `hex.EncodeToString()` and return the result.

You can test this function with the example input `'Hello world'` to get the expected output `'3e25960a79dbc69b674cd4ec67a72c62'`. If you pass an empty string, the function will return `nil`.