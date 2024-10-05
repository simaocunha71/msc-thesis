    result := ""
    for i := 0; i < len(a); i++ {
        var xor byte
        if a[i] == '1' {
            if b[i] == '1' {
                xor = '0'
            } else {
                xor = '1'
            }
        } else {
            if b[i] == '1' {
                xor = '1'
            } else {
                xor = '0'
            }
        }
        result += string(xor)
    }
    return result
}