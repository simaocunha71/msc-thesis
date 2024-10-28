    for i := 0; i < len(s); i++ {
        for j := 0; j < len(s); j++ {
            if s[i] == s[j] && i != j {
                s = strings.Replace(s, s[i:i+1], "", 1)
                break A
            }
        }
    }
    return s
}


func main() {
    input := "AaBbCcDdEe"
    encoded := EncodeCyclic(input)
    decoded := DecodeCyclic(encoded)
    fmt.Println(input)
    fmt.Println(encoded)
    fmt.Println(decoded)
}
