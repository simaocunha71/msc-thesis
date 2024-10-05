    digits := make([]int, 0)
    for x != 0 {
        digits = append(digits, x%10)
        x /= 10
    }
    if len(digits) <= shift {
        for i := 0; i < len(digits); i++ {
            digits = append(digits, digits[i])
        }
        return fmt.Sprint(digits)
    }
    for i, _ := range digits {
        if i == shift {
            shift = len(digits) - 1
        }
    }
    result := make([]int, 0)
    for _, digit := range digits {
        result = append(result, digit)
        if shift == 0 {
            break
        }
        shift--
    }
    return fmt.Sprint(result)
}



