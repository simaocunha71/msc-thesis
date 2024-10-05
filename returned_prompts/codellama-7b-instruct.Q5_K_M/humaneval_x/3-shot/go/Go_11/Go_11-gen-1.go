    var result string
    for i := 0; i < len(a); i++ {
        if a[i] == '1' || b[i] == '1' {
            result += "1"
        } else {
            result += "0"
        }
    }
    return result
}



