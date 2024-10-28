    product := 1
    for n > 0 {
        digit := n % 10
        if digit % 2 != 0 {
            product *= digit
        }
        n /= 10
    }
    return product
}  // or use strconv.Itoa and strings.Split to convert int to string and then split by ""



