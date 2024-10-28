    digits := []rune(strconv.Itoa(x))
    if shift > len(digits) {
        shift = shift % len(digits)
    }
    return string(digits[len(digits)-shift:] + digits[:len(digits)-shift])
}