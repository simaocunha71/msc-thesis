    sum := 0
    product := 1
    if len(numbers) == 0 {
        return [2]int{sum, product}
    }
    for _, n := range numbers {
        sum += n
        product *= n
    }
    return [2]int{sum, product}
}

