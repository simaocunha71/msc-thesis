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
    return fmt.Sprintf("%x", hash.Sum(nil))
}

