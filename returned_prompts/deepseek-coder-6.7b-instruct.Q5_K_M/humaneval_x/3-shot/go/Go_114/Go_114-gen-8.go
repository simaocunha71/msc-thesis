    total_sum := 0
    min_sum := math.MaxInt64

    for _, num := range nums {
        total_sum += num
        if total_sum < min_sum {
            min_sum = total_sum
        }
        total_sum = int(math.Min(float64(total_sum), float64(num)))
    }

    return min_sum
}



