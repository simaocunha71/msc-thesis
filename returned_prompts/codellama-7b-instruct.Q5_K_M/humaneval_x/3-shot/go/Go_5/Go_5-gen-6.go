    if len(numbers) == 0 {
        return make([]int, 0)
    }
    result := make([]int, len(numbers)*2-1)
    for i := 0; i < len(numbers); i++ {
        result[i*2] = numbers[i]
        if i != len(numbers)-1 {
            result[i*2+1] = delimeter
        }
    }
    return result
}



