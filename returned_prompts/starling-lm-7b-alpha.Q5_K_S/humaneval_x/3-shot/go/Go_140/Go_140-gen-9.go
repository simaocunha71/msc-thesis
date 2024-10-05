    result := make([]rune, 0)
    var count int
    for _, r := range text {
        if r == ' ' {
            count++
            if count == 1 {
                result = append(result, '_')
            }else if count > 2 {
                result = append(result, '-')
                count = 2
            }
        }else {
            result = append(result, r)
            count = 0
        }
    }
    return string(result)
}



