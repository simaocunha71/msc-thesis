    digits := []int{}
    num := x
    for num > 0 {
        digits = append([]int{num % 10}, digits...)
        num /= 10
    }
    if shift > len(digits) {
        shift = shift % len(digits)
    }
    return strconv.Itoa(reverse(digits, shift))
}

func reverse(digits []int, shift int) int {
    digits = append([]int{}, digits...)
    for i := 0; i < shift; i++ {
        temp := digits[0]
        digits = digits[1:]
        digits = append([]int{temp}, digits...)
    }
    num := 0
    for i := 0; i < len(digits); i++ {
        num = num*10 + digits[i]
    }
    return num
}