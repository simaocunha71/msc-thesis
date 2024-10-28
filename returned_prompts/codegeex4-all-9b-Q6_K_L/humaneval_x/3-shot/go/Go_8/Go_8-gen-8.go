    var sum int = 0
    var product int = 1

    for _, n := range numbers{
        sum += n
        product *= n
    }
    return [2]int{sum, product}
}



