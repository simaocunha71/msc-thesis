    result := [2]int{}
    sum := 0
    product := 1

    for _, number := range numbers {
        sum += number
        product *= number
    }

    result[0] = sum
    result[1] = product
    return result
}



