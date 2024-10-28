    result := make([]rune, len(a))
    for i := 0; i < len(a); i++ {
        if a[i] == '1' && b[i] == '1' {
            result[i] = '1'
        }else if a[i] == '0' && b[i] == '0' {
            result[i] = '0'
        }else if a[i] == '1' && b[i] == '0' {
            result[i] = '1'
        }else if a[i] == '0' && b[i] == '1' {
            result[i] = '1'
        }
    }
    return string(result)
}



