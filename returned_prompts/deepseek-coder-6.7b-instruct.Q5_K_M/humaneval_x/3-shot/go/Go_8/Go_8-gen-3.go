    sum  := 0
    product := 1

    for _, number := range numbers {
        sum  += number
        product *= number
    }

    return [2]int{sum, product}
}



