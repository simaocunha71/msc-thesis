    max_count := 0
    result := -1

    for _, num := range lst {
        count := 0
        for _, n := range lst {
            if n == num {
                count++
            }
        }
        if count >= num && count > max_count {
            max_count = count
            result = num
        }
    }
    return result
}