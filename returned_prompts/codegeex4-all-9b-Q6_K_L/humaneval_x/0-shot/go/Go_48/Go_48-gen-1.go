package main

import "fmt"

func IsPalindrome(text string) bool {
    length := len(text)
    for i := 0; i < length/2; i++ {
        if text[i] != text[length-1-i] {
            return false
        }
    }
    return true
}

func main() {
    fmt.Println(IsPalindrome(""))
    fmt.Println(IsPalindrome("aba"))
    fmt.Println(IsPalindrome("aaaaa"))
    fmt.Println(IsPalindrome("zbcd"))
}
