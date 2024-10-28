    digits := make([]rune, 0)
    for x > 0 {
        digits = append(digits, rune(x%10))
        x /= 10
    }

    for i := 0; i < shift; i++ {
        digits = append(digits[:1], digits[1:]...)
    }
    return string(digits)
}



