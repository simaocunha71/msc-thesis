    min := math.MaxInt64
    sum := 0

    for _, num := range nums {
        sum += num
        if sum < min {
            min = sum
        }
        sum = int(math.Min(float64(sum), float64(num)))
    }

    return min
}


