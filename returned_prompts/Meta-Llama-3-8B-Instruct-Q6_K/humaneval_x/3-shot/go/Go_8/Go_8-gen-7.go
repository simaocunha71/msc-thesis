    sum := 0
    product := 1

    for _, num := range numbers {
        sum += num
        product *= num
    }

    if len(numbers) == 0 {
        sum = 0
        product = 1
    }

    return [2]int{sum, product}
}