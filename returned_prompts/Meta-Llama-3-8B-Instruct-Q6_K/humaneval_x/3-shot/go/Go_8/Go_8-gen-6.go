    var sum int
    var product int
    for _, value := range numbers {
        sum += value
        product *= value
    }
    if product == 0 {
        product = 1
    }
    return [2]int{sum, product}
}