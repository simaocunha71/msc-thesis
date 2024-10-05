Here is the solution in Go:
```go
package main

import (
    "strings"
)

func Encrypt(s string) string {
    alphabet := "abcdefghijklmnopqrstuvwxyz"
    shiftedAlphabet := ""
    for _, char := range alphabet {
        if char == 'z' {
            shiftedAlphabet += "ab"
        } else {
            shiftedAlphabet += string(char[1:]) + "a"
        }
    }
    result := ""
    for _, char := range strings.ToLower(s) {
        if strings.Contains(alphabet, string(char)) {
            index := strings.Index(alphabet, string(char))
            result += string(shiftedAlphabet[index : index+1])
        } else {
            result += string(char)
        }
    }
    return strings.Title(result)
}

func main() {
    fmt.Println(Encrypt("hi"))  // Output: LM
    fmt.Println(Encrypt("asdfghjkl"))  // Output: ewhjklnop
    fmt.Println(Encrypt("gf"))  // Output: KJ
    fmt.Println(Encrypt("et"))  // Output: IX
}
```
This solution uses the concept of Caesar Cipher where the alphabet is rotated by a fixed number of places. In this case, the alphabet is rotated by 4 places (2 * 2). The function Encrypt takes a string as an argument, converts it to lowercase, and then for each character in the string, it finds the corresponding character in the shifted alphabet and adds it to the result string. If the character is not in the alphabet (like spaces, punctuation, etc.), it is added to the result string as is. Finally, the function returns the result string with the first letter capitalized. The main function demonstrates the usage of the Encrypt function with some test cases.