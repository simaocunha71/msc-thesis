import (
    "strings"
)

func Encrypt(s string) string {
    var encrypted string
    for _, char := range s {
        if char < 'a' || char > 'z' {
            encrypted += string(char)
        } else {
            encrypted += string(char+2*2)
        }
    }
    return encrypted
}

func main() {
    fmt.Println(Encrypt("hello"))
}

