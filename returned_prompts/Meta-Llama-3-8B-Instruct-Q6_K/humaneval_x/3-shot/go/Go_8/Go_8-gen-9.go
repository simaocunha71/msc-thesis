    sum := 0
    product := 1

    for _, num := range numbers {
        sum += num
        product *= num
    }

    return [2]int{sum, product}
}  // or return [2]int{sum, product} if you want to return a tuple directly.