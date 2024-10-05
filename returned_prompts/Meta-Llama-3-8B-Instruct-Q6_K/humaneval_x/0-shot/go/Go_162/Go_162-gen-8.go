Here is the solution:
```go
import (
    "crypto/md5"
    "fmt"
)

func StringToMd5(text string) interface{} {
    if text == "" {
        return nil
    }
    hash := md5.New()
    hash.Write([]byte(text))
    md5sum := hash.Sum(nil)
    return fmt.Sprintf("%x", md5sum)
}
```
Explanation:

* We first check if the input string is empty. If it is, we return `nil`.
* We create a new `md5.New()` object, which is a hash function that generates an MD5 hash.
* We write the input string to the hash function using the `Write()` method.
* We sum the hash values using the `Sum()` method, which returns the hash value as a byte slice.
* We convert the byte slice to a hexadecimal string using the `fmt.Sprintf()` function with the format string `%x`.
* We return the resulting string as the output of the `StringToMd5()` function.

You can test this function with the example you provided:
```go
fmt.Println(StringToMd5("Hello world")) // Output: 3e25960a79dbc69b674cd4ec67a72c62
```