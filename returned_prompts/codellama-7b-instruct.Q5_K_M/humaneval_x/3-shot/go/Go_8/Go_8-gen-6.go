    var sum int = 0
    var prod int = 1
    for _, n := range numbers {
        sum += n
        prod *= n
    }
    return [2]int{sum, prod}
}



