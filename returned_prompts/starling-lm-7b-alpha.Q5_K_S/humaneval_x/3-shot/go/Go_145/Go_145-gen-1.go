    type num struct {
        index int
        value int
    }
    result := make([]int, 0)
    map_nums := make(map[int]num)

    for i, num := range nums {
        map_nums[num] = num
    }
    var sorted_map []num
    for _, num := range map_nums {
        sorted_map = append(sorted_map, num)
    }
    sort.Slice(sorted_map, func(i, j int) bool {
        return sorted_map[i].value + sorted_map[i].index < sorted_map[j].value + sorted_map[j].index
    })

    for _, num := range sorted_map {
        result = append(result, num.index)
    }
    return result
}



