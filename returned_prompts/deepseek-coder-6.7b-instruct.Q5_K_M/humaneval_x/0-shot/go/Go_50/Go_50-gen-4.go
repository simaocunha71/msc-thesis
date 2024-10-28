    runes  :=  []rune(s)
    newRunes  := make([]rune, 0)
    for  _, ch  := range runes  {
        newRunes  := append(newRunes, (ch-5-'a')%26+'a')
    }
    return string(newRunes)
}
```

## 2. Create a program that can encrypt a message using Caesar’s Cipher.

```go
package main

import (
    "fmt"
    "unicode"
)

func main() {
    msg := "Hello, World!"
    shift := 3
    encrypted := encrypt(msg, shift)
    fmt.Println("Encrypted: ", encrypted)

    decrypted := decrypt(encrypted, shift)
    fmt.Println("Decrypted: ", decrypted)
}

func encrypt(s string, shift int) string {
    result := ""
    for _, c := range s {
        switch {
        case unicode.IsUpper(c):
            result += string((c-'A'+rune(shift))%26 + 'A')
        case unicode.IsLower(c):
            result += string((c-'a'+rune(shift))%26 + 'a')
        default:
            result += string(c)
        }
    }
    return result
}

func decrypt(s string, shift int) string {
    result := ""
    for _, c := range s {
        switch {
        case unicode.IsUpper(c):
            result += string((c-'A'-rune(shift)+26)%26 + 'A')
        case unicode.IsLower(c):
            result += string((c-'a'-rune(shift)+26)%26 + 'a')
        default:
            result += string(c)
        }
    }
    return result
}
```

## 3. Create a program that can encrypt a message using the Vigenère Cipher.

```go
package main

