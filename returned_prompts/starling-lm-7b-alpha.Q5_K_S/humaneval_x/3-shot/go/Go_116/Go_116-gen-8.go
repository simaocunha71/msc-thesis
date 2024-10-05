    type item struct {
        num int
        ones int
    }
    result := make([]item, 0)
    for _, v := range arr {
        result = append(result, item{v, count(v)})
    }
    sort.Slice(result, func(i, j int) bool {
        if result[i].ones != result[j].ones {
            return result[i].ones < result[j].ones
        }
        return result[i].num < result[j].num
    })
    result_slice := make([]int, 0)
    for _, item := range result {
        result_slice = append(result_slice, item.num)
    }
    return result_slice
}

func count(n int) int {
    result := 0
    for n != 0 {
        result += n%2
        n /= 2
    }
    return result
}



