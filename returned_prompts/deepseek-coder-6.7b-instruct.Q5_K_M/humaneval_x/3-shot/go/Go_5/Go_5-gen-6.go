    if len(numbers)==0{
        return numbers
    }

    result := make([]int, 0, len(numbers)*(2-1)+1)
    result = append(result, numbers[0])

    for _, number := range numbers[1:] {
        result = append(result, delimeter)
        result = append(result, number)
    }

    return result
}



