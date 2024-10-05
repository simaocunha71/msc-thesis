    var result [2]int

    var sum int = 0
    var product int = 1

    for _, number := range numbers {
        sum += number
        product *= number
    }

    result[0] = sum
    result[1] = product

    return result
}



