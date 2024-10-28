    result := make([]rune, 0)
    binary := decimal / 2
    result = append(result, 'd')
    result = append(result, byte(binary/2+'0'))
    result = append(result, byte(binary%2+'0'))
    result = append(result, 'b')
    return string(result)
}



