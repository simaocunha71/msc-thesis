func StringXor(a string, b string) string {
    lena := len(a)
    lenb := len(b)
    if lena != lenb {
        panic("Invalid input, string lengths must be equal")
    }
    res := make([]byte, lena)
    for i := 0; i < lena; i++ {
        if a[i] != '0' && a[i] != '1' {
            panic("Invalid input, character must be 1 or 0")
        }
        if b[i] != '0' && b[i] != '1' {
            panic("Invalid input, character must be 1 or 0")
        }
        res[i] = a[i] ^ b[i]
    }
    return string(res)
}

// >>> StringXor('010', '110')
// '100'
func StringXor(a string, b string) string {
    lena := len(a)
    lenb := len(b)
    if lena != lenb {
        panic("Invalid input, string lengths must be equal")
    }
    res := make([]byte, lena)
    for i := 0; i < lena; i++ {
        if a[i] != '0' && a[i] != '1' {
            panic("Invalid input, character must be 1 or 0")
        }
        if b[i] != '0' && b[i] != '1' {
            panic("Invalid input, character must be 1 or 0")
        }
        res[i] = a[i] ^ b[i]
    }
    return string(res)
}