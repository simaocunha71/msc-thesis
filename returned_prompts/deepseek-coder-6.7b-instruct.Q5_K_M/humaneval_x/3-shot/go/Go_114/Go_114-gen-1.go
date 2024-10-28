    sum := 0
    min := math.MaxInt64
    for _, num := range nums {
        sum += num
        if sum < min {
            min = sum
        }
        if sum > 0 {
            sum = 0
        }
    }

    return min
}



