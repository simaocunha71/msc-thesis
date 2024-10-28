    product := 1
    for {
        digit := n % 10
        if digit % 2 == 0 {
            product = 0
            break
        }else{
            product *= digit
        }
        n /= 10
        if n == 0 {
            break
        }
    }
    return product
}



