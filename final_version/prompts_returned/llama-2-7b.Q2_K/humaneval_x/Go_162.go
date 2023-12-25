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
    
    md5Text := NewMD5()
    defer md5Text.Finalize()
    
    fmt.Println("Digesting...", text, "=>", md5Text.HexString())
    return md5Text.HexString()
}