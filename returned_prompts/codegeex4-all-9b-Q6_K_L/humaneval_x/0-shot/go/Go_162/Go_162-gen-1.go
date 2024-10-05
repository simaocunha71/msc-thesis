To implement the `StringToMd5` function in Go, you can use the `crypto/md5` package. Here's the complete solution:

```go
package main

import (
	"crypto/md5"
	"encoding/hex"
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

	hasher := md5.New()
	hasher.Write([]byte(text))
	hashInBytes := hasher.Sum(nil)

	return hex.EncodeToString(hashInBytes)
}

func main() {
	fmt.Println(StringToMd5("Hello world")) // Output: 3e25960a79dbc69b674cd4ec67a72c62
}
```

This function works as follows:

1. It first checks if the input string `text` is empty. If it is, it returns `nil`.
2. If `text` is not empty, it creates a new MD5 hash object by calling `md5.New()`.
3. It writes the bytes of the input string `text` to the hash object using `hasher.Write([]byte(text))`.
4. It computes the MD5 hash by calling `hasher.Sum(nil)`, which returns a byte slice representing the hash.
5. It encodes the byte slice into a hexadecimal string using `hex.EncodeToString(hashInBytes)`.
6. Finally, it returns the hexadecimal string representation of the MD5 hash.