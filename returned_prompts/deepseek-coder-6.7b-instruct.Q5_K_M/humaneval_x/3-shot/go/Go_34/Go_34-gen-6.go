    unique_map := make(map[int]struct{})

    for _, v := range l {
        unique_map[v] = struct{}{}
    }

    result := make([]int, 0, len(unique_map))

    for k := range unique_map {
        result = append(result, k)
    }

    sort.Ints(result)

    return result
}



