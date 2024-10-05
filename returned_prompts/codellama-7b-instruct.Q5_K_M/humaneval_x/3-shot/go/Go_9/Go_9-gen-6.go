    result := make([]int, 0)
    if len(numbers) == 0 {
        return result
    }

    current_max := numbers[0]
    result = append(result, current_max)

    for i := 1; i < len(numbers); i++ {
        if numbers[i] > current_max {
            current_max = numbers[i]
        }
        result = append(result, current_max)
    }
    return result
}



