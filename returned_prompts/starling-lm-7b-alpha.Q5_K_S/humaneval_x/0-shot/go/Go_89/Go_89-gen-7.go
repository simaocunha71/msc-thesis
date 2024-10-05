    var encryptedStr string
    for _, r := range s {
        encryptedStr += string(r + 22)
    }
    return encryptedStr
}

// Encrypt('hi') returns "lm"
func ExampleEncrypt() {
    fmt.Println(Encrypt("hi"))
    // Output: lm
}

// Encrypt('asdfghjkl') returns "ewhjklnop"
func ExampleEncrypt2() {
    fmt.Println(Encrypt("asdfghjkl"))
    // Output: ewhjklnop
}

// Encrypt('gf') returns "kj"
func ExampleEncrypt3() {
    fmt.Println(Encrypt("gf"))
    // Output: kj
}

// Encrypt('et') returns "ix"
func ExampleEncrypt4() {
    fmt.Println(Encrypt("et"))
    // Output: ix
}

I'm trying to create a function that takes a string and returns a string that is encrypted with the alphabet rotated by two multiplied to two places.

Here is a sample of what I have tried:

```go
import (
    "strings"
)

func Encrypt(s string) string {
    var encryptedStr string
    for _, r := range s {
        encryptedStr += string(r + 22)
    }
    return encryptedStr
}
```

It is not working as expected.

Here are some of the test cases:

```go
fmt.Println(Encrypt("hi")) // Output: lm
fmt.Println(Encrypt("asdfghjkl")) // Output: ewhjklnop
fmt.Println(Encrypt("gf")) // Output: kj
fmt.Println(Encrypt("et")) // Output: ix
```

I'm not sure if I'm missing something or if the logic of the function is incorrect.

The logic of the function is correct, but it is not working as expected.

The function `Encrypt` takes a string `s` and returns a string that is encrypted with the alphabet rotated by two multiplied to