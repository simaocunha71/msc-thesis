    if base < 2 || base > 9 {
        panic("base must be between 2 and 9")
    }

    digits := []rune{}
    for x > 0 {
        digits = append([]rune{strconv.Itoa(int(x % base))[0]}, digits...)
        x /= base
    }
    return string(digits)
} 