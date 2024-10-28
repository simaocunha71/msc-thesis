    result := make([]int, 0)
    isEven := false
    for _, v := range arr {
        if v % 2 == 0 {
            if !isEven {
                result = append(result, v)
                isEven = true
            }
        }else if isEven {
            result = append(result, v)
            isEven = false
        }
    }
    if len(result) == 0 {
        return []int{}
    }
    if len(result) == 1 {
        return result
    }
    sort(result)
    return result[:1]
}



