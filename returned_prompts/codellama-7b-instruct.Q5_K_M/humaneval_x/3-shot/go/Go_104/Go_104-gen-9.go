    result := make([]int, 0)
    temp := make([]int, 0)
    for i := 0; i < len(x); i++ {
        temp = append(temp, x[i])
    }

    sort.Ints(temp)

    for i := 0; i < len(temp); i++ {
        if temp[i] % 2 != 0 {
            result = append(result, temp[i])
        }
    }
    return result
}



