    result := ""
    for i := 0; i < len(a); i++ {
        if a[i] == '1' && b[i] == '1' {
            result += "0"
        } else if a[i] == '0' && b[i] == '0' {
            result += "0"
        } else {
            result += "1"
        }
    }
    return result
}