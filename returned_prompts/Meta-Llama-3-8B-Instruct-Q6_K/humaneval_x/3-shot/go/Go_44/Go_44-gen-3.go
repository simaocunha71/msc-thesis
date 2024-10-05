    if x == 0 {
        return "0"
    }
    digits := []rune{}
    for x > 0 {
        digit := x % base
        if digit > 9 {
            digit = rune('a' + digit - 10)
        }
        digits = append([]rune{rune(digit + '0')}, digits...)
        x /= base
    }
    return string(digits)
}