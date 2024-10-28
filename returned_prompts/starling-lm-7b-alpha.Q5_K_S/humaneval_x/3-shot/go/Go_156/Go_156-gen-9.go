    if number < 1 || number > 1000 {
        return ""
    }

    result := make([]rune, 0)

    hundreds := number / 100
    result = append(result, hundredsToRoman(hundreds)...)

    tens := number % 100 / 10
    result = append(result, tensToRoman(tens)...)

    ones := number % 10
    result = append(result, onesToRoman(ones)...)

    return string(result)
}

func hundredsToRoman(num int) []rune {
    result := make([]rune, 0)

    if num == 9 {
        result = append(result, 'i', 'c', 'm', 'm')
    }else if num == 8 {
        result = append(result, 'i', 'c', 'm', 'm')
    }else if num == 7 {
        result = append(result, 'v', 'm', 'm', 'm')
    }else if num == 6 {
        result = append(result, 'm', 'm', 'm')
    }else if num == 5 {
        result = append(result, 'm', 'm')
    }else if num == 4 {
        result = append(result, 'm')
    }else if num == 3 {
        result = append(result, 'm')
    }else if num == 2 {
        result = append(result, 'm')
    }else if num == 1 {
        result = append(result, 'm')
    }

    return result
}

func tensToRoman(num int) []rune {
    result := make([]rune, 0)

    if num == 9 {
        result = append(result, 'i', 'c', 'c')
    }else if num == 8 {
        result = append(result, 'i', 'c', 'c')
    }else if num == 7 {
        result = append(result, 'd', 'c', 'c')
    }else if num == 6 {
       