Here is the solution:
```go
import (
    "crypto/md5"
    "fmt"
)

// Given a string 'text', return its md5 hash equivalent string.
// If 'text' is an empty string, return nil.
// 
// >>> StringToMd5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
func StringToMd5(text string) interface{} {
    if text == "" {
        return nil
    }
    hash := md5.New()
    hash.Write([]byte(text))
    md5Bytes := hash.Sum(nil)
    return fmt.Sprintf("%x", md5Bytes)
}
```
Explanation:

1. We first check if the input string `text` is empty. If it is, we return `nil`.
2. We create a new `md5.New()` object, which is an instance of the `md5.Hash` type.
3. We write the input string `text` to the `md5` hash object using the `Write()` method.
4. We call the `Sum()` method on the `md5` hash object to get the hash bytes.
5. We convert the hash bytes to a hexadecimal string using the `fmt.Sprintf()` function with the format string `"%"`.
6. We return the resulting hexadecimal string.

Note that the `md5` package is part of the Go standard library, and the `md5.New()` function creates a new `md5` hash object. The `Write()` method writes data to the hash object, and the `Sum()` method returns the hash bytes. The `fmt.Sprintf()` function is used to convert the hash bytes to a hexadecimal string.