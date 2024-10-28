    result := make([]rune, 0)

    for i := 0; i < len(a); i++ {
        if a[i] == b[i]{
            result = append(result, '0')
        }else{
            result = append(result, '1')
        }
    }
    return string(result)
}



