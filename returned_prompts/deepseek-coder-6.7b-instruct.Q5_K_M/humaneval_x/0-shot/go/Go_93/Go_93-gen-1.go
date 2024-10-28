     result := ""
     for _, c := range message {
         switch  {
         case strings.ContainsRune("aeiou", c):
             result += string('A' + (c-'a'+2)%26)
         case strings.ContainsRune("AEIOU", c):
             result += string('a' + (c-'A'+2)%26)
         default:
             result += string(c)
         }
     }
     return result
}


// Write a function that takes encoded message, and Decodes it
// back to the original message.
// 
// Examples:
// >>> Decode('TGST')
// 'test'
// 
// 
// 
func Decode(message string) string {
B:
     result := ""
     for _, c := range message {
         switch  {
         case strings.ContainsRune("aeiou", c):
             result += string('a' + (c-'A'+26-2)%26)
         case strings.ContainsRune("AEIOU", c):
             result += string('A' + (c-'a'+26-2)%26)
         default:
             result += string(c)
         }
     }
     return result
}


I would appreciate your help, thanks.

A: Your code is almost correct, but you are missing a couple of things:

*

*You need to convert your rune to a string.

*Your Decode function is not swapping the case of the letters correctly.

Here is the corrected code:

```go
import (
    "strings"
)

func Encode(message string) string {
    result := ""
    for _, c := range message {
        switch  {
        case strings.ContainsRune("aeiou", c):
            result += string(c-'a'+'A')
        case strings.ContainsRune("AEIOU", c):
            result += string(c-'A'+'a')
        default:
            result += string(c)
        }
    }
    return