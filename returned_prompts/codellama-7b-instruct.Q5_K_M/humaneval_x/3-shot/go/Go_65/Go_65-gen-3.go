    result := ""
    var digits []rune
    for x > 0 {
        digits = append(digits, rune(x%10 + '0'))
        x = x / 10
    }
    if shift > len(digits){
        for i := len(digits)-1; i >= 0; i-- {
            result += string(digits[i])
        }
    } else {
        for i := len(digits)-1-shift; i >= 0; i-- {
            result += string(digits[i])
        }
        for i := 0; i < shift; i++ {
            result += string(digits[i])
        }
    }
    return result
}



