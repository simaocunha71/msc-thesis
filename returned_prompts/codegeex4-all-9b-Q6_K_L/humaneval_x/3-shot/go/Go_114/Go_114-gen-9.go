    min := math.MaxInt32
    sum := 0

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



