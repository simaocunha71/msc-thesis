    result := make([]int,0)
    var max int
    for i := 0; i < len(numbers); i++ {
        if i == 0 {
            max = numbers[i]
        }else{
            if numbers[i] > max{
                max = numbers[i]
            }
        }
        result = append(result, max)
    }
    return result
}

