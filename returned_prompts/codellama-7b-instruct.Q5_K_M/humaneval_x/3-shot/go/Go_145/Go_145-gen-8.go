    var sum_map = make(map[int]int)

    for _, num := range nums {
        sum_map[num] += num
    }

    keys := make([]int, 0)
    for k := range sum_map {
        keys = append(keys, k)
    }

    sort.Slice(keys, func(i int, j int) bool {
        if sum_map[keys[i]] == sum_map[keys[j]] {
            return i < j
        }
        return sum_map[keys[i]] < sum_map[keys[j]]
    })

    result := make([]int, len(nums))
    for i, k := range keys {
        result[i] = k
    }

    return result
}



