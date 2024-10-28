    result := make([]int, 0)
    for _, v := range x {
        if strconv.Itoa(v)[0]%2 != 0 {
            result = append(result, v)
        }
    }
    sort.Ints(result)
    return result
}



