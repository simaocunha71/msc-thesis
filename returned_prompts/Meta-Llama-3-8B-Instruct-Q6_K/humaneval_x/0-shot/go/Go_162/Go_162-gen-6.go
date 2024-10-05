```go
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

1. We import the `crypto/md5` package, which provides the functionality to compute the MD5 hash of a string.
2. We define a function `StringToMd5` that takes a string `text` as input and returns its MD5 hash equivalent string.
3. If the input string `text` is empty, we return `nil`.
4. We create a new MD5 hash object using `md5.New()`.
5. We write the input string `text` to the hash object using `hash.Write([]byte(text))`.
6. We compute the MD5 sum using `hash.Sum(nil)`, which returns a byte slice representing the hash.
7. We convert the byte slice to a hexadecimal string using `fmt.Sprintf("%x", md5sum)`.
8. We return the resulting string.

Note that the `StringToMd5` function returns an interface{} type, which means it can return either a string or `nil`. If the input string is empty, it returns `nil`, otherwise it returns the MD5 hash string.