    result := make([]rune, len(str))
    for index, character := range str {
        if character >= 'a' && character <= 'z' {
            result[index] = character - 'a' + 'A'
        } else if character >= 'A' && character <= 'Z' {
            result[index] = character - 'A' + 'a'
        } else {
            result[index] = character
        }
    }
    return string(result)
}



