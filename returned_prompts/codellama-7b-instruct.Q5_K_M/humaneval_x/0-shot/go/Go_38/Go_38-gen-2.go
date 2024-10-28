    for i := 0; i < len(s); i++ {
        if s[i] == ':' {
            return s[:i]
        }
    }
    return s
}

func main() {
    fmt.Println(DecodeCyclic(EncodeCyclic(":)))")))
}
