    current_sum :=  0
    min_sum := math.MaxInt64

    for _, num := range nums {
        current_sum += num
        if current_sum < min_sum {
            min_sum = current_sum
        }
        current_sum = int(math.Min(float64(current_sum), float64(num)))
    }

    return min_sum
}



