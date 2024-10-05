    result := make([]int, 0, len(numbers)*(2-1)+1)
    if len(numbers) > 0 {
        result = append(result, numbers[0])
        for _, num := range numbers[1:] {
            result = append(result, delimeter)
            result = append(result, num)
        }
    }
    return result
}



