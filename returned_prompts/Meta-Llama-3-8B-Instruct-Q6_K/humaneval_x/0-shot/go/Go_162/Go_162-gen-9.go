Here is the solution:
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
    digest := hash.Sum(nil)
    return hex.EncodeToString(digest[:])
}

func main() {
    fmt.Println(StringToMd5("Hello world")) // Output: 3e25960a79dbc69b674cd4ec67a72c62
}
```


Explanation:
The `StringToMd5` function takes a string `text` as input and returns its MD5 hash equivalent string. If `text` is an empty string, the function returns `nil`.

The function uses the `crypto/md5` package to create a new MD5 hash object `hash`. It then writes the input string `text` to the hash object using the `Write` method. The `Sum` method is used to get the hash digest, which is a byte array.

The `encoding/hex` package is used to encode the hash digest as a hexadecimal string. The `EncodeToString` function is used to convert the byte array to a string.

In the `main` function, we test the `StringToMd5` function with the input string "Hello world" and print the output. The output should be the MD5 hash equivalent string of "Hello world".