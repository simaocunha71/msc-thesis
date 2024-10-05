    var sum int = 0
    var product int = 1

    for _, i := range numbers {
        sum += i
        product *= i
    }
    return [2]int{sum, product}
}



