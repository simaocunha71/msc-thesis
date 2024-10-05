    type pair struct {
        value int
        count int
    }
    result := make([]int, 0)
    value_list := make(map[int]pair)
    for _, v := range arr {
        if _, ok := value_list[v]; !ok {
            value_list[v] = pair{v, len(fmt.Sprint(v)) - len(fmt.Sprint(v & v - 1))}
        }
    }
    for _, v := range value_list {
        result = append(result, v.value)
    }
    sort.Slice(result, func(i int, j int) bool {
        if value_list[result[i]].count != value_list[result[j]].count {
            return value_list[result[i]].count < value_list[result[j]].count
        }
        return result[i] < result[j]
    })
    return result
}



