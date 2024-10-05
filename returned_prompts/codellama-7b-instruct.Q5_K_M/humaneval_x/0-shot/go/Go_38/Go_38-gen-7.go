    for {
        if s == "" {
            break A
        }
        runes := []rune(s)
        if len(runes) > 0 {
            s = string(append(runes[1:], runes[0]))
        }
    }
    return s
}

func main() {
    fmt.Println(EncodeCyclic(""))
    fmt.Println(EncodeCyclic("a"))
    fmt.Println(EncodeCyclic("ab"))
    fmt.Println(EncodeCyclic("abc"))
    fmt.Println(EncodeCyclic("abcd"))
    fmt.Println(EncodeCyclic("abcde"))
    fmt.Println(EncodeCyclic("abcdef"))
    fmt.Println(EncodeCyclic("abcdefg"))
    fmt.Println(EncodeCyclic("abcdefgh"))
    fmt.Println(EncodeCyclic("abcdefghi"))
    fmt.Println(EncodeCyclic("abcdefghij"))
    fmt.Println(EncodeCyclic("abcdefghijk"))
    fmt.Println(EncodeCyclic("abcdefghijkl"))
    fmt.Println(EncodeCyclic("abcdefghijklm"))
    fmt.Println(EncodeCyclic("abcdefghijklmn"))
    fmt.Println(EncodeCyclic("abcdefghijklmno"))
    fmt.Println(EncodeCyclic("abcdefghijklmnop"))
    fmt.Println(EncodeCyclic("abcdefghijklmnopq"))
    fmt.Println(EncodeCyclic("abcdefghijklmnopqr"))
    fmt.Println(EncodeCyclic("abcdefghijklmnopqrs"))
    fmt.Println(EncodeCyclic("abcdefghijklmnopqrst"))
    fmt.Println(EncodeCyclic("abcdefghijklmnopqrstu"))
    fmt.Println(EncodeCyclic("abcdefghijklmnopqr