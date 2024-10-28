    var result []int = make([]int, len(arr))
    copy(result, arr)
    sort.Slice(result, func(i, j int) bool {
        a := fmt.Sprintf("%b", result[i])
        b := fmt.Sprintf("%b", result[j])

        if len(a) > len(b) {
            return false
        }else if len(a) < len(b) {
            return true
        }else {
            for k := len(a) - 1; k >= 0; k-- {
                if a[k] > b[k] {
                    return false
                }else if a[k] < b[k] {
                    return true
                }
            }
            return result[i] < result[j]
        }
    })
    return result
}



