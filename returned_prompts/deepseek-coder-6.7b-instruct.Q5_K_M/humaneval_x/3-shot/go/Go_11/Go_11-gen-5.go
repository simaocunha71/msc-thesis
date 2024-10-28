    result := ""
    for i:=0; i<len(a); i++ {
        if a[i] != b[i] {
            result += "1"
        } else {
            result += "0"
        }
    }
    return result
}



