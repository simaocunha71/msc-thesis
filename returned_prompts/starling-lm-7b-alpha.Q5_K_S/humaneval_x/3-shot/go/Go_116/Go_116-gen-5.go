    type ByOnes struct{
        Ones int
        Value int
    }
    result := make([]int, 0)
    for _, v := range arr {
        b := ByOnes{Ones: countOnes(v), Value: v}
        result = append(result, b)
    }
    sort.Slice(result, func(i int, j int) bool {
        if result[i].Ones == result[j].Ones {
            return result[i].Value < result[j].Value
        }
        return result[i].Ones < result[j].Ones
    })
    res := make([]int, 0)
    for _, v := range result {
        res = append(res, v.Value)
    }
    return res
}

func countOnes(num int) int {
    result := 0
    for num > 0 {
        if num % 2 == 1 {
            result += 1
        }
        num /= 2
    }
    return result
}








































































































































































































































































