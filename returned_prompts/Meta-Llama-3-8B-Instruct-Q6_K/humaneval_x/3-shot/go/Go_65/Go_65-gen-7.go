    digits := []int{}
    num := x
    for num > 0 {
        digits = append(digits, num % 10)
        num /= 10
    }
    for shift > len(digits) {
        shift -= len(digits)
    }
    if shift > 0 {
        digits = append(digits[len(digits)-shift:], digits[:len(digits)-shift]...)
    }
    result := ""
    for _, digit := range digits {
        result += strconv.Itoa(digit)
    }
    return result
}