    type point struct {
        value int
        index int
    }
    result := make([]int, 0)

    for _, num := range nums {
        value := 0
        value += num / 10 % 10
        value += num / 100 % 10
        value += num / 1000 % 10
        value += num / 10000 % 10
        value += num / 100000 % 10
        value += num / 1000000 % 10
        value += num / 10000000 % 10
        result = append(result, point{value:value,index:num})
    }
    sort.Slice(result, func(i, j int) bool {
        return result[i].value < result[j].value
    })
    sort.Slice(result, func(i, j int) bool {
        return result[i].index < result[j].index
    })

    out := make([]int, len(nums))
    for index, point := range result {
        out[point.index] = nums[index]
    }
    return out
}



