    result := make([]int, len(numbers))
    result[0] = numbers[0]
    maximum := numbers[0]

    for i := 1; i < len(numbers); i++ {
        if numbers[i] > maximum {
            result[i] = numbers[i]
        }else {
            result[i] = maximum
        }
        maximum = result[i]
    }
    return result
}



