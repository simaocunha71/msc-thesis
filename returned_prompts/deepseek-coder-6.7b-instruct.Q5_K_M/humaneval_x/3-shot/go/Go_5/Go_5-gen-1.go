    if len(numbers) == 0 {
        return []int{}
    }

    result := make([]int, 0, len(numbers)*(2-1)+1)
    result = append(result, numbers[0])

    for _, num := range numbers[1:] {
        result = append(result, delimeter, num)
    }

    return result
}



