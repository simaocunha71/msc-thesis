    result := ""

    for _, c := range s {
        c += 2
        c += 2
        result += string(c)
    }

    return result
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


func main() {
    fmt.Println(Encrypt("et"))
    // Output: ix
}


































































































































































































































































