    result := make([]int, len(numbers))
    result[0] = numbers[0]

    for i := 1; i < len(numbers); i++ {
        if numbers[i] > numbers[i-1] {
            result[i] = numbers[i]
        }else{
            result[i] = result[i-1]
        }
    }
    return result
}



