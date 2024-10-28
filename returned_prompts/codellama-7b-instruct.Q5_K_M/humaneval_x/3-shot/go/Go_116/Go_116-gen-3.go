    var result []int
    var result_map = make(map[int][]int)
    for _, v := range arr {
        ones := 0
        for _, c := range fmt.Sprintf("%b", v) {
            if c == '1' {
                ones++
            }
        }
        result_map[ones] = append(result_map[ones], v)
    }
    keys := make([]int, 0)
    for k := range result_map {
        keys = append(keys, k)
    }
    sort.Ints(keys)

    for _, k := range keys {
        sort.Ints(result_map[k])
        result = append(result, result_map[k]...)
    }
    return result
}



