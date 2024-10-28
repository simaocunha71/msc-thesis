    result := make([]int, len(numbers))
    for i := 0; i < len(numbers); i++ {
        if i == 0 {
            result[i] = numbers[i]
        } else {
            if numbers[i] > result[i-1] {
                result[i] = numbers[i]
            } else {
                result[i] = result[i-1]
            }
        }
    }
    return result
}



