    product := 1
    for n > 0 {
        remainder, _ := strconv.Atoi(strconv.Itoa(n)%10)
        if remainder % 2 != 0 {
            product *= remainder
        }
        n /= 10
    }
    return product
}