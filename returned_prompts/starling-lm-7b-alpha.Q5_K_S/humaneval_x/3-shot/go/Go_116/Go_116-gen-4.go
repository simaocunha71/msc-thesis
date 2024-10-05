    type ByCount struct {
        Count int
        Value int
    }
    type ByValue struct {
        Value int
    }

    result := make([]int, len(arr))
    copy(result, arr)
    sort.Slice(result, func(i int, j int) bool {
        left := result[i]
        right := result[j]
        if count1 := ByCount{}.Count(left); count1 == ByCount{}.Count(right) {
            return ByValue{}.Value(left) < ByValue{}.Value(right)
        }
        return ByCount{}.Count(left) < ByCount{}.Count(right)
    })
    return result
}



