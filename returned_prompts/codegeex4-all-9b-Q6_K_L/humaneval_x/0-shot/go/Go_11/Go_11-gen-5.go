func StringXor(a string, b string) string {
    if a == b {
        return "0"
    }
    if a == "1" {
        return b
    }
    if b == "1" {
        return a
    }
    return "0"
}