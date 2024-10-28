    digits := []rune(strconv.Itoa(x))
    shift = shift % len(digits)
    if shift > 0 {
        digits = append(digits[len(digits)-shift:], digits[:len(digits)-shift]...)
    }
    return string(digits)
}