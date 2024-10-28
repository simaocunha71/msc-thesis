    var sum int
    var product int
    product = 1
    for _, value := range numbers {
        sum += value
        product *= value
    }
    return [2]int{sum, product}
}



