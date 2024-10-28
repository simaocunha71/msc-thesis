    var result []byte
    var prev bool

    for _, c := range text {
        if c == ' ' {
            if prev {
                result = append(result, '-')
            } else {
                result = append(result, '_')
            }
            prev = true
        } else {
            result = append(result, c)
            prev = false
        }
    }
    return string(result)
}