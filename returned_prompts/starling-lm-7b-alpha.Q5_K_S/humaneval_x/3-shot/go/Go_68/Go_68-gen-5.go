    result := make([]int, 0)

    for i, v := range arr {
        if v % 2 == 0 {
            result = append(result, []int{v, i} )
        }
    }

    if len(result) == 0 {
        return result
    }

    min_v := result[0][0]
    min_i := result[0][1]
    for _, v := range result {
        if v[0] < min_v {
            min_v = v[0]
            min_i = v[1]
        } else if v[0] == min_v {
            if v[1] < min_i {
                min_i = v[1]
            }
        }
    }

    return []int{min_v, min_i}
}



