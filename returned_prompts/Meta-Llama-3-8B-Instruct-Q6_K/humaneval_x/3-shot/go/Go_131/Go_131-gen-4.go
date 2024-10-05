    product := 1
    for n > 0 {
        digit := n % 10
        if digit % 2 != 0 {
            product *= digit
        }
        n /= 10
    }
    return product
} 

// or
func Digits(n int) int {
    product := 1
    for n > 0 {
        digit, _ := strconv.Atoi(string(rune(n%10)))
        if digit % 2 != 0 {
            product *= digit
        }
        n /= 10
    }
    return product
} 





