    max_count := 0
    max_number := -1

    for _, num := range lst {
        count := 0
        for _, num2 := range lst {
            if num2 == num {
                count += 1
            }
        }
        if count >= num && count > max_count {
            max_count = count
            max_number = num
        }
    }
    if max_number == -1 {
        return -1
    }
    return max_number
}