    product := 1
    for {
        d, err := strconv.Atoi(strconv.Itoa(n % 10))
        if err != nil {
            return 0
        }
        if d % 2 != 0 {
            product *= d
        }
        n /= 10
        if n == 0 {
            break
        }
    }
    return product
}



