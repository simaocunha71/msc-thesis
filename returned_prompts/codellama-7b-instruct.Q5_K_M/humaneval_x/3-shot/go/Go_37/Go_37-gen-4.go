    even_index := make([]int, 0)
    odd_index := make([]int, 0)

    for i, v := range l {
        if i%2 == 0 {
            even_index = append(even_index, v)
        } else {
            odd_index = append(odd_index, v)
        }
    }

    sort.Ints(even_index)
    result := make([]int, 0)
    for _, v := range odd_index {
        result = append(result, v)
    }
    for _, v := range even_index {
        result = append(result, v)
    }
    return result
}



