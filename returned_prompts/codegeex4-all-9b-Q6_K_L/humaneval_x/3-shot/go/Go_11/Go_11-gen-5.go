    result := ""
    for i := range a {
        if a[i] == b[i] {
            result += "0"
        } else {
            result += "1"
        }
    }
    return result
}



