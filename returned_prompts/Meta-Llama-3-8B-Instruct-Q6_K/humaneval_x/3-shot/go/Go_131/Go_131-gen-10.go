    product := 1
    for ; n > 0; n = n / 10 {
        digit := n % 10
        if digit % 2 != 0 {
            product *= digit
        }
    }
    return product
}

// Alternative solution using strconv.Atoi
func Digits(n int) int {
    product := 1
    for ; n > 0; n = n / 10 {
        str := strconv.Itoa(n % 10)
        digit, _ := strconv.Atoi(str)
        if digit % 2 != 0 {
            product *= digit
        }
    }
    return product
}