    var result string
    if len(a) != len(b) {
        fmt.Println("Error: Strings are not the same length")
        return ""
    }
    for i := 0; i < len(a); i++ {
        if a[i] == b[i] {
            result += "0"
        } else {
            result += "1"
        }
    }
    return result
}

