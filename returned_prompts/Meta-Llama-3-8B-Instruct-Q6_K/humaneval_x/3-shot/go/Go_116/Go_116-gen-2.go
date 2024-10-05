    type pair struct {
        num int
        ones int
    }

    var result []pair
    for _, num := range arr {
        result = append(result, pair{num, bitsOnes(num)})
    }
    sort.Slice(result, func(i, j int) bool {
        if result[i].ones != result[j].ones {
            return result[i].ones < result[j].ones
        }
        return result[i].num < result[j].num
    })
    result2 := make([]int, 0)
    for _, pair := range result {
        result2 = append(result2, pair.num)
    }
    return result2
}

func bitsOnes(num int) int {
    count := 0
    for num > 0 {
        if num & 1 == 1 {
            count++
        }
        num >>= 1
    }
    return count
}