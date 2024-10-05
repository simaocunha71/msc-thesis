    result := make([]rune, len(a))
    for i:=0; i<len(a); i++ {
        if a[i] == '0' {
            if b[i] == '0' {
                result[i] = '0'
            }else {
                result[i] = '1'
            }
        }else {
            if b[i] == '0' {
                result[i] = '1'
            }else {
                result[i] = '0'
            }
        }
    }
    return string(result)
}



