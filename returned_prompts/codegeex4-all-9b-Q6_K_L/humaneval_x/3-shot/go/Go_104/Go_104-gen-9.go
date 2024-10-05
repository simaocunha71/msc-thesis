    result := make([]int, 0)
    for _, value := range x{
        has_even := false
        for _, digit := range strconv.Itoa(value){
            if digit % 2 == 0{
                has_even = true
                break
            }
        }
        if !has_even{
            result = append(result, value)
        }
    }
    sort.Ints(result)
    return result
}



