    result := make([]int, 0)

    for _, num := range l {
        if num > 0 {
            result = append(result, num)
        }
    }

    return result
}



