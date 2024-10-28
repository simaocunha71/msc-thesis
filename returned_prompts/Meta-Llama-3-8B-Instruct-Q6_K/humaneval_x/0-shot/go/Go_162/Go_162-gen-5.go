Here is a Go program that implements the `StringToMd5` function as described:
```go
package main

import (
    "crypto/md5"
    "encoding/hex"
    "fmt"
    "strings"
)

// Given a string 'text', return its md5 hash equivalent string.
// If 'text' is an empty string, return nil.
func StringToMd5(text string) interface{} {
    if text == "" {
        return nil
    }
    hash := md5.New()
    hash.Write([]byte(text))
    digest := hash.Sum(nil)
    return hex.EncodeToString(digest[:])
}

func main() {
    fmt.Println(StringToMd5("Hello world")) // Output: 3e25960a79dbc69b674cd4ec67a72c62
}
```
Here's a brief explanation of the code:

1. We import the necessary packages: `crypto/md5` for the MD5 hashing algorithm, `encoding/hex` for converting the byte array to a hexadecimal string, and `fmt` for printing the result.
2. The `StringToMd5` function takes a string `text` as input and returns its MD5 hash equivalent string.
3. If the input `text` is an empty string, we return `nil`.
4. We create a new MD5 hash object using `md5.New()`.
5. We write the input `text` to the hash object using `hash.Write([]byte(text))`.
6. We get the hash digest using `hash.Sum(nil)`, which returns a byte array.
7. We convert the byte array to a hexadecimal string using `hex.EncodeToString(digest[:])`.
8. In the `main` function, we test the `StringToMd5` function with the input "Hello world" and print the result.