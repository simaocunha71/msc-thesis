    var sum int = 0
    var product int = 1
    for _, number := range numbers {
        sum += number
        product *= number
    }
    return [2]int{sum, product}
}



