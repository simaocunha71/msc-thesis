    for i := 0; i < len(s); i++ {
        if s[i] != s[i+1] {
            s = s[:i] + string(s[i+1]) + s[i:]
            goto A
        }
    }
    return s
}

func main() {
    encoded := EncodeCyclic("This is a test")
    fmt.Println(encoded)
    fmt.Println(DecodeCyclic(encoded))
}

