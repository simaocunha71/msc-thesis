    digits := []rune(strconv.Itoa(x))
    shift = shift % len(digits)
    if shift == 0 {
        return string(digits)
    }
    return string(digits[shift:]) + string(digits[:shift])
} 



