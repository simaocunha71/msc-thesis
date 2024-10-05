    result := make([]rune, 0)

    previous_space := false
    for _, c := range text {
        if c != ' ' {
            result = append(result, c)
            previous_space = false
        }else if previous_space && len(result) >= 2 && result[len(result)-2:] == []rune("-_") {
            result[len(result)-2] = '-'
        }else if previous_space {
            result = append(result, '_')
        }else {
            previous_space = true
        }
    }
    return string(result)
}



