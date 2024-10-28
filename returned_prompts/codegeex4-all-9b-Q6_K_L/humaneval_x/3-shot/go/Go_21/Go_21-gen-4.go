    min := numbers[0]
    max := numbers[0]
    for _, v := range numbers {
        if v < min {
            min = v
        }
        if v > max {
            max = v
        }
    }

    for i, v := range numbers {
        numbers[i] = (v - min) / (max - min)
    }
    return numbers
}

