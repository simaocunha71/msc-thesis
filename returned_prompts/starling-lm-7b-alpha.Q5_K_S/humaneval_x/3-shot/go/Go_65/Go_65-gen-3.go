    digits := make([]rune, 0)
    for i := x; i > 0; i /= 10 {
        digits = append(digits, rune(i % 10 + '0'))
    }
    shift = shift % len(digits)
    if shift > 0 {
        digits = append(digits[:shift], digits[len(digits)-shift:]...)
    }else {
        digits = append(digits[len(digits)-shift:], digits[:shift]...)
    }

    return string(digits)
}



