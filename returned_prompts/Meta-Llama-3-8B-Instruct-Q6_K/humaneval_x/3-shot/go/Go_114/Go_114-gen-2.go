    min_sum := math.MaxInt32
    current_sum := 0

    for _, num := range nums {
        current_sum += num
        min_sum = int(math.Min(float64(min_sum), float64(current_sum)))
        if current_sum < 0 {
            current_sum = 0
        }
    }

    return min_sum
}