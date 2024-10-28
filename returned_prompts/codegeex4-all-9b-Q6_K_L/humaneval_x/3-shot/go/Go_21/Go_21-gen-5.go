    min := math.Inf(0)
    max := math.Inf(-1)

    for _, n := range numbers {
        if n < min {
            min = n
        }
        if n > max {
            max = n
        }
    }

    for i, n := range numbers {
        numbers[i] = (n - min) / (max - min)
    }

    return numbers
}



