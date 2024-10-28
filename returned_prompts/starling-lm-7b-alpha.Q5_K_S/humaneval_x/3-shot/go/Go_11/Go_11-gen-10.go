    result := make([]rune, 0)

    for i, _ := range a {
        if a[i] == '1' && b[i] == '1' {
            result = append(result, '1')
        }else if a[i] == '0' && b[i] == '0' {
            result = append(result, '0')
        }else {
            result = append(result, '1')
        }
    }
    return string(result)
}



