    total := 0
    min := math.MaxInt64
    for _, num := range nums {
        total += num
        if total < min {
            min = total
        }
        if total > 0 {
            total = 0
        }
    }
    return min
}



