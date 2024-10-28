    digits := []rune(strconv.Itoa(x))
    n := len(digits)
    shift = shift % n
    if shift > 0 {
        digits = append(digits[n-shift:], digits[:n-shift]...)
    }
    return string(digits)
}