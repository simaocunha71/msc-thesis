    result := make([]int, len(lst))
    copy(result, lst)
    sort.Slice(result, func(i, j int) bool {
        if result[i] < result[j] {
            return true
        } else if result[i] > result[j] {
            return false
        } else {
            if i < j {
                return true
            } else {
                return false
            }
        }
    })
    return result
}



