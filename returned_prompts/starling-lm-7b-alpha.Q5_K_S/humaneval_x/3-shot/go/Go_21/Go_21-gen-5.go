    min_num := numbers[0]
    max_num := numbers[0]
    for _, num := range numbers {
        if num < min_num {
            min_num = num
        }
        if num > max_num {
            max_num = num
        }
    }
    result := make([]float64, len(numbers))
    for i, num := range numbers {
        result[i] = (num - min_num)/(max_num - min_num)
    }
    return result
}



