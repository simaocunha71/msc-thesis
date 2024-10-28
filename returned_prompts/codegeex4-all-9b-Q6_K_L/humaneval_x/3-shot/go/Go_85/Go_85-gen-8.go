    sum := 0
    for i := 0; i < len(lst); i++ {
        if lst[i] % 2 == 0 && i % 2 == 1 {
            sum += lst[i]
        }
    }
    return sum
}

