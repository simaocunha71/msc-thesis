    var result []byte

    for i := 0; i < len(a); i++ {
        if a[i] != b[i] {
            result = append(result, '1')
        }else{
            result = append(result, '0')
        }
    }
    return string(result)
}



