    if base < 0 || base > 9 {
        return "base must be between 0 and 9"
    }

B:
    if x < 0 {
        return "x must be non-negative"
    }

C:
    if x == 0 {
        return "0"
    }

D:
    // convert to string
    s := strconv.Itoa(x)

E:
    // convert to base
    baseDigit := s[len(s)-1:]
    baseString := baseDigit
    for _, digit := range s[:len(s)-1] {
        baseDigit := strconv.Itoa(digit)
        baseString = baseDigit + baseString
    }

F:
    return baseString
}
