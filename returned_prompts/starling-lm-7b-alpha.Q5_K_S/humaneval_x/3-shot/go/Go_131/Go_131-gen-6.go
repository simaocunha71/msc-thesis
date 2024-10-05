    digits := []int{}
    for n > 0 {
        digits = append(digits, n%10)
        n /= 10
    }
    product := 1
    for _, digit := range digits {
        if digit%2 == 1 {
            product *= digit
        }
    }
    return product
}



