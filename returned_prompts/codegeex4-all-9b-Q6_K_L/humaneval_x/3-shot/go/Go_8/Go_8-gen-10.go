    var sum, product int = 0, 1
    for _, n := range numbers {
        sum += n
        product *= n
    }
    return [2]int{sum, product}
}



