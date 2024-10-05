    result := ""
    for i := 0; i < len(a); i++ {
        if a[i] == b[i] {
            result += "0"
        } else {
            result += "1"
        }
    }
    return result
}



